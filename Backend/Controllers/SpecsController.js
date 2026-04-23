const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse/sync");

const csvPath = path.join(__dirname, "../laptops.csv");
const csvData = fs.readFileSync(csvPath, "utf8");
const laptops = parse(csvData, { columns: true, skip_empty_lines: true });

console.log(`Loaded ${laptops.length} laptops from database`);

function scoreMatch(laptop, search) {
  const fullName = `${laptop.brand} ${laptop.name}`.toLowerCase();
  const words = search.toLowerCase().split(" ").filter(Boolean);
  let score = 0;

  for (const word of words) {
    if (fullName.includes(word)) score += 2;
    if (laptop.brand?.toLowerCase().includes(word)) score += 1;
    if (laptop.name?.toLowerCase().includes(word)) score += 1;
  }

  return score;
}

function getUniqueSuggestions(scored, skip = 0, limit = 3) {
  const seen = new Set();
  const suggestions = [];

  for (const item of scored.slice(skip)) {
    if (suggestions.length >= limit) break;
    const fullName = `${item.laptop.brand} ${item.laptop.name}`;

    const cleanName = fullName
      .replace(/\b[A-Z0-9]{6,}\b/g, "") 
      .replace(/\s+/g, " ")
      .trim();

    const baseKey = cleanName.split(" ").slice(0, 3).join(" ").toLowerCase();

    if (!seen.has(baseKey)) {
      seen.add(baseKey);
      suggestions.push(cleanName);
    }
  }

  return suggestions;
}


exports.getLaptopSpecs = async (req, res) => {
  const { model } = req.query;
  if (!model) return res.status(400).json({ error: "Model name required" });

  const search = model.toLowerCase().trim();

  const scored = laptops
    .map((laptop) => ({ laptop, score: scoreMatch(laptop, search) }))
    .filter((item) => item.score > 0)
    .sort((a, b) => b.score - a.score);

  if (scored.length === 0) {
    return res.json({ found: false, specs: null, suggestions: [] });
  }

  const best = scored[0];

  if (best.score >= 3) {
    const match = best.laptop;
    const specs = {
      cpu: match.CPU || match.processor || null,
      gpu: match.GPU || null,
      ram: match.Ram ? `${match.Ram} ${match.Ram_type || ""}`.trim() : null,
      storage: match.ROM ? `${match.ROM} ${match.ROM_type || ""}`.trim() : null,
      display: match.display_size
        ? `${match.display_size} inch ${parseInt(match.resolution_width)}x${parseInt(match.resolution_height)}`
        : null,
      os: match.OS || null,
    };

    const suggestions = getUniqueSuggestions(scored, 1, 3);

    return res.json({
      found: true,
      specs,
      modelFound: `${match.brand} ${match.name}`,
      suggestions
    });
  }

  const suggestions = getUniqueSuggestions(scored, 0, 4);

  return res.json({ found: false, specs: null, suggestions });
};