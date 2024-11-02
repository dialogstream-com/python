#!/bin/bash

# Ensure script fails on any error
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting publication process...${NC}"

# Check if we're in a clean git state
if [[ -n $(git status -s) ]]; then
    echo -e "${RED}Error: Git working directory is not clean${NC}"
    echo "Please commit or stash your changes first"
    exit 1
fi

# Clean up previous builds
echo -e "${GREEN}Cleaning up previous builds...${NC}"
rm -rf build/ dist/ *.egg-info/

# Install/upgrade build tools
echo -e "${GREEN}Upgrading build tools...${NC}"
python -m pip install --upgrade pip build twine

# Build the package
echo -e "${GREEN}Building package...${NC}"
python -m build

# Check the distribution
echo -e "${GREEN}Checking distribution...${NC}"
twine check dist/*

# Ask for confirmation before publishing
read -p "Do you want to publish to PyPI? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo -e "${GREEN}Publishing to PyPI...${NC}"
    twine upload dist/*
    
    # Create and push git tag
    VERSION=$(python setup.py --version)
    echo -e "${GREEN}Creating and pushing git tag v$VERSION...${NC}"
    git tag -a "v$VERSION" -m "Release version $VERSION"
    git push origin "v$VERSION"
    
    echo -e "${GREEN}Publication completed successfully!${NC}"
else
    echo -e "${RED}Publication aborted${NC}"
fi