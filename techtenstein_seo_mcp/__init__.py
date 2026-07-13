"""Techtenstein SEO Audit MCP Server.

Wraps the Techtenstein SEO Audit REST API and exposes it as an MCP tool.
Claude, Cline, Cursor, and any MCP-compatible client can invoke `seo_audit`
to run on-page SEO analysis on any URL.

Install:
    pip install fastmcp requests
    export TECHTENSTEIN_API_KEY=your_key

Run:
    python server.py

Or via uvx:
    uvx techtenstein-seo-mcp
"""

import os
import sys
import requests
from fastmcp import FastMCP

API_BASE = os.getenv("TECHTENSTEIN_SEO_API_BASE", "https://seo.api.techtenstein.com")
API_KEY = os.getenv("TECHTENSTEIN_API_KEY", "")

mcp = FastMCP(
    name="techtenstein-seo",
    version="1.0.0",
    description="On-page SEO audit for any URL. Powered by Techtenstein SEO API.",
)


@mcp.tool()
def seo_audit(url: str) -> dict:
    """
    Run a complete on-page SEO audit for a URL.

    Returns:
      - Title tag content, length, optimization score
      - Meta description content and length
      - Open Graph tag coverage
      - Heading hierarchy (H1/H2/H3 counts)
      - Word count and keyword density
      - Image alt-text coverage percentage
      - Internal/external link ratios
      - Overall SEO score (0-100)
      - Prioritized fix recommendations

    Args:
      url: The URL to audit (must include https://).

    Returns:
      Structured JSON with all SEO metrics.
    """
    if not url.startswith(("http://", "https://")):
        return {"error": "URL must include http:// or https://"}

    headers = {"X-API-Key": API_KEY} if API_KEY else {}
    try:
        r = requests.get(
            f"{API_BASE}/audit",
            params={"url": url},
            headers=headers,
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def seo_batch_audit(urls: list[str]) -> list[dict]:
    """
    Run SEO audits on multiple URLs in one call.

    Args:
      urls: List of URLs to audit (max 20 per call).

    Returns:
      List of audit results, one per URL.
    """
    if len(urls) > 20:
        return [{"error": "Max 20 URLs per batch call"}]
    return [seo_audit(url) for url in urls]


if __name__ == "__main__":
    if not API_KEY:
        print("WARNING: TECHTENSTEIN_API_KEY not set. Free tier only (100 calls/day).", file=sys.stderr)
    mcp.run()
