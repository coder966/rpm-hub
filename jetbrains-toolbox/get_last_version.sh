#!/bin/sh
set -eu

apiResponse="$(curl -fsSL 'https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release')"
# Toolbox archive filenames include the full build number.
latestVersion="$(printf '%s' "${apiResponse}" | jq -er '.TBA[0].build | select(type == "string" and test("^[0-9]+(\\.[0-9]+)+$"))')"

printf '%s\n' "$latestVersion"
