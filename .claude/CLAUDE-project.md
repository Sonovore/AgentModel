
# AgentModel Project

Research and development of agent orchestration patterns for Claude Code.

## Project Focus

- Agent task breakdown and delegation
- Context window management
- Multi-agent coordination
- Human-in-the-loop workflows

## Principles

1. **Tasks fit in one context window** - If they don't, break them down further
2. **Human supervises (for now)** - Automation after trust is built
3. **File-based coordination** - No external dependencies, git-friendly
4. **Incremental complexity** - Start simple, add features as needed

## Reference

- `docs/` - Design documents and research notes
- `scripts/` - Prototype scripts and tools
- `tasks/` - Task definitions and templates
