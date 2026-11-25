// This entry is a tiny delivery step for the "Post the Meme, Win the Feed"
// bounty: it just moves the X post's address from the repo into the place the
// bounty gate looks for it.
// The bot dir defaults to /bot and the output dir to /output, both overridable
// via MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR. It validates the post JSON has a
// usable url and then writes it out, exiting non-zero on any problem.

const { mkdirSync, readFileSync, writeFileSync } = require("node:fs");
const { join } = require("node:path");

function fail(message: string): never {
  console.error(`error: ${message}`);
  process.exit(1);
}

try {
  const botDir: string = process.env.MAKEFUN_BOT_DIR ?? "/bot";
  const outputDir: string = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

  mkdirSync(outputDir, { recursive: true });

  const postPath = join(botDir, "POST.json");
  let raw: string;
  try {
    raw = readFileSync(postPath, "utf8");
  } catch {
    fail(`could not read ${postPath}`);
  }

  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch {
    fail(`${postPath} is not valid JSON`);
  }

  if (
    typeof parsed !== "object" ||
    parsed === null ||
    Array.isArray(parsed) ||
    typeof (parsed as Record<string, unknown>).url !== "string" ||
    ((parsed as Record<string, unknown>).url as string).trim() === ""
  ) {
    fail(`POST.json must be an object with a non-empty string "url" field`);
  }

  const outPath = join(outputDir, "POST.json");
  writeFileSync(outPath, JSON.stringify(parsed, null, 2) + "\n", "utf8");

  console.log(`wrote ${outPath} with url: ${(parsed as Record<string, string>).url}`);
  process.exit(0);
} catch (err) {
  fail(err instanceof Error ? err.message : String(err));
}
