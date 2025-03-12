#!/bin/bash

set -e

# Move to project root
cd "$(dirname "$0")/.."

# File to update version in
SETUP_FILE="./tools/setup.py"

# Extract current version
CURRENT_VERSION=$(grep "version=" $SETUP_FILE | sed -E "s/.*version='([0-9]+)\.([0-9]+)\.([0-9]+)'.*/\1.\2.\3/")
MAJOR=$(echo $CURRENT_VERSION | cut -d. -f1)
MINOR=$(echo $CURRENT_VERSION | cut -d. -f2)
PATCH=$(echo $CURRENT_VERSION | cut -d. -f3)

echo "🔍 Current version is: v$CURRENT_VERSION"
read -p "➡️  Increment (M)ajor, (m)inor, or (p)atch version? [M/m/p]: " CHOICE

if [[ "$CHOICE" == "M" ]]; then
  NEW_MAJOR=$((MAJOR + 1))
  NEW_MINOR=0
  NEW_PATCH=0
elif [[ "$CHOICE" == "m" ]]; then
  NEW_MAJOR=$MAJOR
  NEW_MINOR=$((MINOR + 1))
  NEW_PATCH=0
elif [[ "$CHOICE" == "p" ]]; then
  NEW_MAJOR=$MAJOR
  NEW_MINOR=$MINOR
  NEW_PATCH=$((PATCH + 1))
else
  echo "❌ Invalid choice. Aborting."
  exit 1
fi

NEW_VERSION="$NEW_MAJOR.$NEW_MINOR.$NEW_PATCH"
TAG="v$NEW_VERSION"

echo "📦 Updating version to $NEW_VERSION in $SETUP_FILE..."
sed -i '' "s/version='.*'/version='$NEW_VERSION'/" $SETUP_FILE

echo "📄 Committing changes..."
git add $SETUP_FILE README.md CHANGELOG.md .env.example ssh_manager/
git commit -m "Release $TAG"

echo "🏷️  Creating tag $TAG"
git tag $TAG

echo "🚀 Pushing to GitHub..."
git push origin main --tags

echo "🎉 Release $TAG published successfully!"