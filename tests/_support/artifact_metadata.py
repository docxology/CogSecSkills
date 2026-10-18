"""Shared real inputs for artifact metadata tests."""

from __future__ import annotations

import shutil

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]

__all__ = ["PROJECT_ROOT", "pytest", "shutil"]
