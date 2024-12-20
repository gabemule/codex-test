#!/bin/bash

mkdir -p .tmp &&

# Define files to exclude from changelog
# These are typically auto-generated or non-essential for changelog
EXCLUDE_PATHSPEC=":(exclude)yarn.lock :(exclude)package-lock.json :(exclude)pnpm-lock.yaml :(exclude)*.pyc :(exclude)__pycache__/** :(exclude).env :(exclude)dist/** :(exclude)build/** :(exclude)*.log :(exclude).DS_Store :(exclude)coverage/** :(exclude).nyc_output/** :(exclude)*.min.js :(exclude)*.min.css :(exclude)_old/**"

last_commit_hash=$(git rev-parse HEAD) &&

log_commit() {
    local commit_hash=$1
    local is_merge=$2
    echo ""
    echo "${is_merge:+Merge }Commit: $commit_hash"
    git show --pretty=format:"%an - %ad%n%s%n%b" --name-status $commit_hash -- . $EXCLUDE_PATHSPEC
    echo ""
    echo "-----------------------------------------"
}

if [ $(git rev-list --parents -n 1 $last_commit_hash | wc -w) -gt 2 ]; then
    {
        log_commit $last_commit_hash "Merge"
        
        parent1=$(git rev-parse $last_commit_hash^1)
        parent2=$(git rev-parse $last_commit_hash^2)
        
        echo "New Commits Introduced by This Merge:"
        echo ""
        
        git log --pretty=format:"%H" --reverse $parent1..$last_commit_hash | while read commit; do
            log_commit $commit
        done
    } > .tmp/git_log_simple.txt
else
    {
        log_commit $last_commit_hash
    } > .tmp/git_log_simple.txt
fi &&

echo "=========================================" >> .tmp/git_log_simple.txt
