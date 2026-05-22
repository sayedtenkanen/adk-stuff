#!/usr/bin/env bash
set -euo pipefail
staged=$(git diff --cached --name-only --diff-filter=ACM)
[ -z "$staged" ] && exit 0
if echo "$staged" | xargs grep -rnE \
  -e '-----BEGIN (RSA )?PRIVATE KEY-----' \
  -e 'sk-[A-Za-z0-9_=-]{20,}' \
  -e 'pk-[A-Za-z0-9_=-]{20,}' \
  -e 'gh[pso]_[A-Za-z0-9_=-]{36,}' \
  -e 'AKIA[0-9A-Z]{16}' \
  /dev/null; then
  echo "SECURITY: Found potential secrets in staged files. Remove them before committing."
  exit 1
fi
exit 0
