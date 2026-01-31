# Reddit Research Tool

A Python script for collecting posts from AI-related subreddits for a university design project researching AI development and the changing landscape of social media in the age of bots.

## Project Context

This tool supports a design student's research project examining:
- How AI development is discussed in online communities
- The changing nature of social media as AI agents/bots become more prevalent
- Community reactions to emerging AI technologies

## Features

- Search specific subreddits for relevant posts
- Get hot/trending posts from research subreddits
- Read-only access (no posting, commenting, or voting)
- Export results to JSON for analysis
- Low API usage (~50-100 requests/day)

## Research Subreddits

The following subreddits are monitored for AI-related discussions:

1. r/OpenAI - OpenAI and GPT discussions
2. r/Anthropic - Anthropic and Claude discussions
3. r/singularity - AI singularity and future tech
4. r/accelerate - AI acceleration community
5. r/ClaudeAI - Claude AI user community
6. r/LocalLLaMA - Local/open-source LLM community
7. r/ThatsInsane - Mainstream reactions to tech

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a Reddit app at https://www.reddit.com/prefs/apps
2. Choose "script" as the app type
3. Copy your `client_id` and `client_secret`
4. Update the credentials in `reddit_search.py`

## Usage

```bash
# List research subreddits
python reddit_search.py --list-subs

# Search r/OpenAI for "AI agents"
python reddit_search.py "AI agents" --subreddit OpenAI

# Get hot posts from r/singularity
python reddit_search.py --hot -s singularity

# Search and save to file
python reddit_search.py "bots social media" -s Anthropic -o results.json
```

## License

For educational/personal use only. University design project.
