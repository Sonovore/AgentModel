# Bibliography System

**Created:** 2026-01-20
**Model:** Claude Sonnet 4.5

This directory contains a comprehensive bibliography system for all mental model research in the AgentModel project.

---

## Files

### 1. BIBLIOGRAPHY.md (168 KB)
**Master bibliography** containing all unique sources across the research corpus.

- **1,407 unique sources** (deduplicated from 1,502 total citations)
- Organized into 8 categories
- Alphabetized within each category
- Sources from **68 research documents** across **22 disciplines**

**Categories:**
- Books (54)
- Academic Papers (54)
- Military Doctrine & Government Documents (165)
- Reports & White Papers (12)
- Academic Websites & Institutions (75)
- Wikipedia (82)
- Websites & Online Resources (699)
- Other (266)

### 2. CITATION-INDEX.md (180 KB)
**Cross-reference index** mapping each source to the mental model documents that cite it.

- 1,403 indexed sources (some sources appeared in automation/metadata sections)
- Shows which research documents use which sources
- Essential for citation management if converting to book format

**Example usage:**
If you need to know which mental models cite a specific source, search for the source title in this file.

### 3. BIBLIOGRAPHY-QUALITY-NOTES.md (11 KB)
**Quality control document** highlighting issues that need human review before book publication.

**Critical issues flagged:**
- Only 4 citations include ISBN/DOI out of 1,407 sources
- 266 sources in "Other" category need recategorization
- Inconsistent author name formatting
- Missing access dates for websites
- 26 documents without sources sections

**Recommendation:** Review this document before converting research to book format.

---

## Research Coverage Statistics

### Documents by Discipline

| Discipline | Doc Count | Citations in Index |
|-----------|-----------|-------------------|
| Management | 18 | 55 |
| Air Traffic Control | 4 | 126 |
| Orchestral Conducting | 4 | 116 |
| Agile/Scrum | 3 | 105 |
| Jazz Improvisation | 4 | 104 |
| Theater Stage Management | 4 | 83 |
| Surgical Teams | 3 | 77 |
| Logistics/Supply Chain | 4 | 75 |
| Kitchen Brigade | 3 | 73 |
| Military Planning | 5 | 69 |
| Lean Manufacturing | 3 | 65 |
| Military Command | 4 | 62 |
| Military Coordination | 5 | 61 |
| Pedagogy | 3 | 59 |
| Military Doctrine | 5 | 45 |
| (and 14 more disciplines) | | |

**Total:** 94 markdown documents, 68 with sources sections

---

## How to Use

### For Research
1. **Finding sources by topic:** Open `BIBLIOGRAPHY.md` and search by category or keyword
2. **Finding which models use a source:** Open `CITATION-INDEX.md` and search for the source title
3. **Checking citation quality:** Review `BIBLIOGRAPHY-QUALITY-NOTES.md`

### For Book Preparation
1. Review `BIBLIOGRAPHY-QUALITY-NOTES.md` for critical issues
2. Add ISBNs to all book citations (see quality notes for list)
3. Add DOIs to all academic paper citations
4. Recategorize sources in "Other" category
5. Standardize author name formatting to "Last, First" format
6. Add access dates to website citations

### For Adding New Research
When creating new mental model research documents:

1. **Add a "Sources" or "References" section** at the end of your document
2. **Format citations as markdown list items:**
   ```markdown
   ## Sources

   - Author. *Title*. Publisher, Year. ISBN XXX.
   - [Web Title](URL)
   ```
3. **Run the extraction script** to update the bibliography:
   ```bash
   python3 .claude/scripts/extract_sources.py
   ```

---

## Automation

### Extraction Script
**Location:** `.claude/scripts/extract_sources.py`

**What it does:**
- Scans all markdown files in `docs/` (excluding READMEs)
- Extracts "Sources" or "References" sections
- Parses and categorizes citations automatically
- Deduplicates based on URL or title
- Generates three output files

**To regenerate the bibliography:**
```bash
cd /Users/chrishector/SonovoreDrive/Sonovore/AgentModel
python3 .claude/scripts/extract_sources.py
```

**Output:**
```
Found 94 research documents
Extracted 1,502 citations from 68 documents
Unique sources (after deduplication): 1,407

Created bibliography: docs/BIBLIOGRAPHY.md
Created citation index: docs/CITATION-INDEX.md
```

### Automatic Categorization
The script categorizes sources based on content analysis:

- **Books:** Looks for publisher names, ISBN, edition numbers
- **Papers:** Looks for journal names, DOI, arXiv
- **Military/Government:** Looks for .mil, .gov, doctrine keywords
- **Wikipedia:** Direct Wikipedia URL detection
- **Academic Web:** .edu domains, university sites
- **Websites:** Default for URLs
- **Other:** Citations without clear category

---

## Citation Format Standards

### Books
```
Author, First. *Title*. Publisher, Year. ISBN XXX.
```
Example:
```
Coram, Robert. *Boyd: The Fighter Pilot Who Changed the Art of War.*
Back Bay Books, 2002. ISBN 978-0316796880.
```

### Academic Papers
```
Author, First. "Title." *Journal Name*, Volume(Issue), Pages. DOI: XXX.
```
Example:
```
Simon, Herbert A. "A Behavioral Model of Rational Choice."
*Quarterly Journal of Economics* 69, no. 1 (1955): 99-118.
DOI: 10.2307/1884852.
```

### Military Doctrine
```
[Document Number] Title, Edition, Date
```
Example:
```
ADP 6-0 Mission Command, U.S. Army (2019)
```

### Websites
```
[Title](URL)
```
With access date for book publication:
```
Author. "Title." Website Name. URL. Accessed YYYY-MM-DD.
```

---

## Known Issues

1. **Limited ISBN/DOI coverage:** Only 4 citations include these identifiers. Needs human addition.

2. **Large "Other" category:** 266 sources need manual categorization review.

3. **Author name inconsistency:** Mix of "Last, First" and "First Last" formats.

4. **No access dates:** Website citations lack access dates (required for some citation styles).

5. **Duplicate detection limitations:** Script uses URL or title for deduplication, which may miss some duplicates with different URLs or slight title variations.

---

## Future Enhancements

### Potential Improvements
- Add ISBN/DOI lookup via API (CrossRef, OpenLibrary)
- Improve categorization with LLM-based analysis
- Add citation style conversion (APA, Chicago, MLA)
- Implement broken link checking
- Generate BibTeX format for LaTeX users
- Add citation count analytics
- Track citation trends across disciplines

### For Book Publication
- Professional copyediting of citations
- Verification of all ISBNs
- DOI addition for academic papers
- Access date standardization
- Author name normalization
- Publisher verification
- Edition information completion

---

## Maintenance

### When to Regenerate
Run the extraction script when:
- New research documents are added
- Existing documents have updated sources
- Manual corrections are made to source sections in documents

### Quality Control
Periodically review:
- `BIBLIOGRAPHY-QUALITY-NOTES.md` for new issues
- Citation format consistency
- Category accuracy
- Deduplication effectiveness

---

## Questions or Issues?

This bibliography system was created using Claude Sonnet 4.5. The extraction script is Python-based and requires no external dependencies beyond the standard library.

For issues or questions about the bibliography system, review the extraction script at `.claude/scripts/extract_sources.py` which includes detailed documentation.
