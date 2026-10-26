import { readFile } from "node:fs/promises";

const data = JSON.parse(await readFile("data/evals.json", "utf8"));
console.log(data.evals.length, "evals, licence:", data.license);
const coding = data.evals.filter((e) => e.category === "Coding");
console.log(coding.length, "coding evals, e.g.", coding[0].name);
