# Insights — Pakistan Election Turnout Analysis (2008–2018)

## Key Findings
- The largest turnout increases (2008→2018) were concentrated in Punjab, 
  particularly Multan, Gujranwala, and Toba Tek Singh constituencies, 
  each rising over 20 percentage points.
- [Add 1-2 more sentences based on your province_avg_swing.png chart — 
  which province had the highest average swing?]

## Method
Constituency-level turnout data from Pakistan's 2008, 2013, and 2018 
general elections were linked using a two-stage entity resolution 
process: exact name matching (12 constituencies), followed by 
province-constrained fuzzy string matching using RapidFuzz at a 75% 
confidence threshold (143 additional constituencies). This was 
necessary because the 2018 delimitation redrew National Assembly 
boundaries, changing constituency numbering and names 
(e.g., NA-1 was "Peshawar 1" in 2008/2013 but "Chitral" in 2018).

## Limitations
155 of 266 constituencies (58%) were confidently linked across all 
three elections. The remaining 111 (42%) could not be automatically 
matched due to seat splits, merges, or renaming from the 2018 
delimitation, and are documented in unmatched_constituencies.csv 
for manual review.