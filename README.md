# SRE CI/CD Demo

![CI Pipeline](https://github.com/danielarojasone/sre-cicd-demo/actions/workflows/ci.yml/badge.svg)

## Overview

This project demonstrates a basic CI/CD pipeline using GitHub Actions for a Python-based SRE utility.

## Pipeline Jobs

### lint

Runs `flake8` to validate code quality, syntax, unused imports, and basic PEP8 compliance.

### test

Runs unit tests using `pytest` and validates code coverage using `pytest-cov`.

The pipeline requires a minimum coverage threshold of 80%.

## Design Decisions

### Why Flake8?

Flake8 is lightweight, fast, and appropriate for CI pipelines. It provides quick feedback for syntax and style issues without the heavier configuration required by Pylint.

### Why separate jobs?

The lint and test jobs run independently and in parallel. This provides faster feedback and makes failures easier to identify.

### Why 80% coverage?

An 80% threshold is a practical balance between quality and speed. It encourages meaningful test coverage without forcing unrealistic 100% coverage for a small demo project.

### Why a build badge?

The badge provides immediate visibility into pipeline health, which is useful for SRE practices focused on reliability, automation, and operational transparency.