<!-- mcp-name: io.github.sathvic-kollu/techtenstein-seo -->

# Techtenstein SEO MCP

MCP server that gives your Claude, Cline, or Cursor session access to on-page SEO audits
for any URL. Powered by the [Techtenstein SEO Audit API](https://apis.techtenstein.com).

## Tools exposed

- `seo_audit(url)` — Full on-page SEO audit for a single URL
- `seo_batch_audit(urls)` — Batch audit up to 20 URLs

## Install (Claude Desktop)

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "techtenstein-seo": {
      "command": "uvx",
      "args": ["techtenstein-seo-mcp"],
      "env": {
        "TECHTENSTEIN_API_KEY": "your_key_from_techtenstein.com"
      }
    }
  }
}
```

Restart Claude Desktop. `seo_audit` and `seo_batch_audit` will appear as available tools.

## Install (Cline / VS Code)

Cline auto-detects MCP servers from your Claude Desktop config. Same setup as above works.

## Install (Cursor)

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "techtenstein-seo": {
      "command": "uvx",
      "args": ["techtenstein-seo-mcp"],
      "env": {"TECHTENSTEIN_API_KEY": "your_key"}
    }
  }
}
```

## Get an API key

Free tier (100 audits/day, no card): https://apis.techtenstein.com

Paid tiers start at $5/month for 5,000 audits.

## Example usage

Once installed, ask Claude:

> "Run an SEO audit on https://techtenstein.com and tell me the top 3 things to fix."

Claude will call `seo_audit`, receive the JSON response, and synthesize recommendations.

Or batch:

> "Audit these 5 competitor pages and compare their SEO scores: [urls]"

Claude will call `seo_batch_audit`, receive all 5 results, and produce a comparison table.

## Response schema

```json
{
  "url": "https://example.com",
  "seo_score": 84,
  "title": {"content": "...", "length": 58, "optimal": true},
  "meta_description": {"content": "...", "length": 145},
  "headings": {"h1": 1, "h2": 5, "h3": 12},
  "word_count": 2367,
  "images": {"total": 15, "with_alt": 12, "alt_coverage": 80},
  "links": {"internal": 24, "external": 8},
  "recommendations": ["...", "..."]
}
```

## Support

- Docs: https://apis.techtenstein.com
- Issues: https://github.com/sathvic-kollu/techtenstein-seo-mcp/issues
- Email: sathvic777@gmail.com

## License

MIT
