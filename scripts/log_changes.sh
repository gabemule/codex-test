#!/bin/bash

mkdir -p .tmp &&
last_commit_hash=$(git rev-parse HEAD) &&

log_commit() {
    local commit_hash=$1
    local is_merge=$2
    echo ""
    echo "${is_merge:+Merge }Commit: $commit_hash"
    git show --pretty=format:"%an - %ad%n%s%n%b" --name-status $commit_hash -- . ':(exclude)yarn.lock' ':(exclude)_old'
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
    } > .tmp/commit_changes_log.txt
else
    {
        log_commit $last_commit_hash
    } > .tmp/commit_changes_log.txt
fi &&

echo "=========================================" >> .tmp/commit_changes_log.txt
