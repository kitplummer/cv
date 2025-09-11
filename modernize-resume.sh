#!/bin/bash

# Script to modernize the resume HTML with custom CSS

# Generate the HTML using the existing Makefile
make html

# Create a modernized version with inline CSS
if [ -f "kp-resume.html" ]; then
    # Read the CSS file
    CSS_CONTENT=$(cat resume-modern.css)
    
    # Create a temporary file with the modernized HTML
    cat kp-resume.html | sed "/<style type=\"text\/css\">/,/<\/style>/c\\
<style type=\"text/css\">\\
${CSS_CONTENT}\\
</style>" > kp-resume-modern.html
    
    # Replace the original file
    mv kp-resume-modern.html kp-resume.html
    
    echo "✓ HTML modernized with custom CSS"
else
    echo "Error: kp-resume.html not found"
    exit 1
fi

# Generate PDF from the modernized HTML
make pdf

echo "✓ Resume modernization complete!"