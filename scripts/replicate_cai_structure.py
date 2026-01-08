#!/usr/bin/env python3
"""
Replicate CAI Directory Structure Across Repository

This script replicates the comprehensive CAI template structure from the
100-00_TEMPLATES_SSoT_QMS subsystem to all other CAI directories in the
repository, ensuring consistent integration workflows across all subsystems.

Usage:
    python scripts/replicate_cai_structure.py [--dry-run] [--verbose]
"""

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import List, Set


# Template source directory
TEMPLATE_CAI_DIR = (
    "02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/"
    "FAMILY/Q100_STD01/DOMAIN/OOO-OS-ONTOLOGIES-OFFICE/SYSTEMS/100-GENERAL/"
    "SUBSYSTEMS/100-00_TEMPLATES_SSoT_QMS/PLM/CAx/CAI"
)

# Directories to create in each CAI folder
CAI_DIRECTORIES = [
    "SCRIPTS",
    "APPLICATIONS",
    "PROCESS_DEFINITIONS",
    "TOOLCHAINS/plm_adapter",
    "TOOLCHAINS/cam_recipes",
    "TOOLCHAINS/test_harness",
    "INTEGRATION_TESTS/smoke",
    "INTEGRATION_TESTS/regression",
    "EXPORTS/step_ap242",
    "EXPORTS/packaging",
    "MANUFACTURING_SIM",
    "QA",
    "DOCS",
]

# Files to copy from template
TEMPLATE_FILES = {
    "README.md": "README.md",
    "META.json": "META.json",
    "SCRIPTS/export_step_ap242.sh": "SCRIPTS/export_step_ap242.sh",
    "SCRIPTS/generate_assembly_instructions.py": "SCRIPTS/generate_assembly_instructions.py",
    "SCRIPTS/run_integration_test.py": "SCRIPTS/run_integration_test.py",
    "APPLICATIONS/README.md": "APPLICATIONS/README.md",
    "APPLICATIONS/co2_battery_examples.py": "APPLICATIONS/co2_battery_examples.py",
    "PROCESS_DEFINITIONS/assembly_sequence.yaml": "PROCESS_DEFINITIONS/assembly_sequence.yaml",
    "PROCESS_DEFINITIONS/test_procedure.yaml": "PROCESS_DEFINITIONS/test_procedure.yaml",
    "DOCS/CAI_GUIDE.md": "DOCS/CAI_GUIDE.md",
    "DOCS/INTERFACES.md": "DOCS/INTERFACES.md",
}


def find_cai_directories(repo_root: Path) -> List[Path]:
    """Find all CAI directories in the repository."""
    cai_dirs = []
    for cai_path in repo_root.rglob("**/PLM/CAx/CAI"):
        if cai_path.is_dir():
            cai_dirs.append(cai_path)
    return sorted(cai_dirs)


def get_subsystem_info(cai_path: Path) -> str:
    """Extract subsystem identifier from CAI path."""
    parts = cai_path.parts
    # Find SUBSYSTEMS in path and get the next part
    for i, part in enumerate(parts):
        if part == "SUBSYSTEMS" and i + 1 < len(parts):
            return parts[i + 1]
    return "UNKNOWN"


def should_skip_directory(cai_path: Path, template_path: Path) -> bool:
    """Determine if a directory should be skipped."""
    # Skip the template directory itself
    return cai_path == template_path


def has_existing_structure(cai_path: Path) -> bool:
    """Check if CAI directory already has substantial content."""
    # Check if it has more than just a simple README
    files = list(cai_path.glob("*"))
    if len(files) == 0:
        return False
    if len(files) == 1 and files[0].name == "README.md":
        return False
    # If it has subdirectories like SCRIPTS, APPLICATIONS, etc., consider it structured
    subdirs = [f for f in files if f.is_dir()]
    structured_subdirs = set(["SCRIPTS", "APPLICATIONS", "PROCESS_DEFINITIONS", "DOCS"])
    has_structure = any(d.name in structured_subdirs for d in subdirs)
    return has_structure


def create_directory_structure(cai_path: Path, dry_run: bool = False, verbose: bool = False):
    """Create the CAI directory structure."""
    for dir_path in CAI_DIRECTORIES:
        full_path = cai_path / dir_path
        if not full_path.exists():
            if verbose:
                print(f"  Creating directory: {dir_path}")
            if not dry_run:
                full_path.mkdir(parents=True, exist_ok=True)


def copy_template_files(
    cai_path: Path,
    template_path: Path,
    dry_run: bool = False,
    verbose: bool = False,
    force: bool = False
):
    """Copy template files to target CAI directory."""
    subsystem = get_subsystem_info(cai_path)

    for src_rel, dst_rel in TEMPLATE_FILES.items():
        src_file = template_path / src_rel
        dst_file = cai_path / dst_rel

        if not src_file.exists():
            if verbose:
                print(f"  Warning: Template file not found: {src_rel}")
            continue

        # Skip if file exists and we're not forcing
        if dst_file.exists() and not force:
            if verbose:
                print(f"  Skipping existing file: {dst_rel}")
            continue

        if verbose:
            print(f"  Copying: {src_rel} -> {dst_rel}")

        if not dry_run:
            # Read content and customize for subsystem
            content = src_file.read_text()

            # Replace template subsystem name with actual subsystem
            content = content.replace("100-00_TEMPLATES_SSoT_QMS", subsystem)

            # Write to destination
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            dst_file.write_text(content)

            # Preserve executable permissions for scripts
            if src_file.suffix in [".sh", ".py"] and os.access(src_file, os.X_OK):
                dst_file.chmod(0o755)


def replicate_cai_structure(
    repo_root: Path,
    dry_run: bool = False,
    verbose: bool = False,
    force: bool = False,
    skip_existing: bool = True
):
    """Main function to replicate CAI structure across all directories."""
    template_path = repo_root / TEMPLATE_CAI_DIR

    if not template_path.exists():
        print(f"Error: Template directory not found: {template_path}")
        return 1

    print(f"Finding all CAI directories in: {repo_root}")
    cai_dirs = find_cai_directories(repo_root)
    print(f"Found {len(cai_dirs)} CAI directories")

    if dry_run:
        print("\n*** DRY RUN MODE - No changes will be made ***\n")

    skipped_count = 0
    processed_count = 0
    error_count = 0

    for cai_path in cai_dirs:
        relative_path = cai_path.relative_to(repo_root)

        # Skip template directory
        if should_skip_directory(cai_path, template_path):
            if verbose:
                print(f"Skipping template directory: {relative_path}")
            skipped_count += 1
            continue

        # Check if directory already has structure
        if skip_existing and has_existing_structure(cai_path):
            if verbose:
                print(f"Skipping directory with existing structure: {relative_path}")
            skipped_count += 1
            continue

        try:
            print(f"\nProcessing: {relative_path}")
            subsystem = get_subsystem_info(cai_path)
            print(f"  Subsystem: {subsystem}")

            # Create directory structure
            create_directory_structure(cai_path, dry_run, verbose)

            # Copy template files
            copy_template_files(cai_path, template_path, dry_run, verbose, force)

            processed_count += 1

        except Exception as e:
            print(f"  Error processing {relative_path}: {e}")
            error_count += 1

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Total CAI directories: {len(cai_dirs)}")
    print(f"  Processed: {processed_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    print(f"{'='*60}")

    return 0 if error_count == 0 else 1


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Replicate CAI directory structure across repository"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed progress information"
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing files"
    )
    parser.add_argument(
        "--no-skip-existing",
        action="store_true",
        help="Process directories even if they have existing structure"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory (default: current directory)"
    )

    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    if not repo_root.exists():
        print(f"Error: Repository root does not exist: {repo_root}")
        return 1

    return replicate_cai_structure(
        repo_root,
        dry_run=args.dry_run,
        verbose=args.verbose,
        force=args.force,
        skip_existing=not args.no_skip_existing
    )


if __name__ == "__main__":
    sys.exit(main())
