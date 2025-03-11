#!/bin/bash

set -e

echo "\n🔁 Installing in editable mode..."
pip install -e .

echo "\n✅ Committing and tagging release v0.1.5"
git add .
git commit -m "Release v0.1.5"
git tag v0.1.5

echo "\n🚀 Pushing to remote (main branch + tag)"
git push origin main --tags

echo "\n🎉 Release completed."
