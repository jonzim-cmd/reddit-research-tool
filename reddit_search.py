#!/usr/bin/env python3
"""
Reddit Research Tool
A script for collecting posts from AI-related subreddits
for a university design project on AI development and 
the changing landscape of social media in the age of bots.

Usage:
    python reddit_search.py "AI agents" --subreddit OpenAI
    python reddit_search.py "bots" --subreddit singularity
"""

import praw
import argparse
import json
from datetime import datetime

# Subreddits relevant for AI/social media research
RESEARCH_SUBREDDITS = [
    "OpenAI",
    "Anthropic", 
    "singularity",
    "accelerate",
    "ClaudeAI",
    "LocalLLaMA",
    "ThatsInsane"
]


def create_reddit_client():
    """Create Reddit API client."""
    return praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="reddit-research-tool/1.0 (university design project)"
    )


def search_subreddit(reddit, subreddit_name, query, limit=25):
    """Search a subreddit for posts matching query."""
    subreddit = reddit.subreddit(subreddit_name)
    results = []
    
    for post in subreddit.search(query, limit=limit):
        results.append({
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "permalink": f"https://reddit.com{post.permalink}",
            "created": datetime.fromtimestamp(post.created_utc).isoformat(),
            "num_comments": post.num_comments,
            "selftext": post.selftext[:500] if post.selftext else None
        })
    
    return results


def get_hot_posts(reddit, subreddit_name, limit=25):
    """Get hot posts from a subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    results = []
    
    for post in subreddit.hot(limit=limit):
        results.append({
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "permalink": f"https://reddit.com{post.permalink}",
            "created": datetime.fromtimestamp(post.created_utc).isoformat(),
            "num_comments": post.num_comments
        })
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Search Reddit for AI/social media research"
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--subreddit", "-s", default="OpenAI", 
                        help="Subreddit to search")
    parser.add_argument("--limit", "-l", type=int, default=25, 
                        help="Max results")
    parser.add_argument("--output", "-o", help="Output JSON file")
    parser.add_argument("--hot", action="store_true", 
                        help="Get hot posts instead of search")
    parser.add_argument("--list-subs", action="store_true",
                        help="List research subreddits")
    
    args = parser.parse_args()
    
    if args.list_subs:
        print("Research subreddits:")
        for sub in RESEARCH_SUBREDDITS:
            print(f"  r/{sub}")
        return
    
    reddit = create_reddit_client()
    
    if args.hot:
        results = get_hot_posts(reddit, args.subreddit, args.limit)
    else:
        if not args.query:
            parser.error("query required unless using --hot or --list-subs")
        results = search_subreddit(reddit, args.subreddit, args.query, args.limit)
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Saved {len(results)} results to {args.output}")
    else:
        for post in results:
            print(f"[{post['score']}] {post['title']}")
            print(f"    {post['permalink']}\n")


if __name__ == "__main__":
    main()
