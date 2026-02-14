# 🔍 Case File: Operation Beetcoin Network - PART 2 🔍

**FROM:** Special Agent Dwight K. Schrute III  

**TITLE:** Assistant Regional Manager / Volunteer Deputy Sheriff

**TO:** Assistant to the Special Agent (YOU)  

**RE:** URGENT - Advanced Network Analysis Required  

**CONFIDENTIAL**

![Special Agent Dwight K. Schrute](img/dw.jpg)

---

**Listen up, Assistant.**

Good work on Part 1. You've identified the gang. The boss, the collector, the associates - I have all their names and IDs. The basic investigation is complete.

BUT HERE'S THE PROBLEM: The District Attorney looked at your evidence and said, "Dwight, I need MORE! I need to see EVERYONE. Not just the gang members you identified - I need the complete picture. All 100 members of this premium elite service. Every single one of them."

So here's what we're doing now. We're building a **Complete Transaction Network Analysis Matrix**. This is advanced forensic accounting, Assistant. Pay attention.

---

## 📁 DATA FILES

Your investigation will use the following data files:

**Transaction Records:**
- File: `transactions.txt`
- Format: Each line contains `from:ID|to:ID|amount:VALUE`
- Example: `from:27|to:84|amount:2489` means member ID 27 sent $2489 to member ID 84

**Member Information:**
- Files: `members/member_ID0.txt` through `members/member_ID99.txt` (100 files total)
- Format:
  - Line 1: Full name
  - Line 2: Address
- Example: `member_ID42.txt` contains the name and address for the member with ID 42

---

## 🎯 THE ASSIGNMENT

I need you to create a matrix that shows the **average amount of money** sent between **every pair of members** in this entire operation - all 100 members, IDs 0 through 99.

**What does this mean?**

- If Jane Smith (ID 5) sent money to Michael Scott (ID 23) THREE times ($1000, $2000, $3000), the average is $2000.00
- If Jim Halpert (ID 42) sent money to Pam Beesly (ID 8) ONCE ($500), the average is $500.00  
- If Dwight Schrute (ID 15) NEVER sent money to Stanley Hudson (ID 67), we show 0.00

This matrix will reveal the ENTIRE network - not just the gang we identified in Part 1. The DA wants to see the big fish AND the small fish. The active criminals AND the quiet ones. Everyone who's part of this exclusive 100-member operation.

The DA will use this in court. "Ladies and gentlemen of the jury, you can see RIGHT HERE that the defendant sent an average of $5,000 per transaction to the boss. This wasn't a one-time mistake. This was a PATTERN."

---

## 📊 REQUIRED OUTPUT FORMAT

You will create a file called **the_matrix.txt**

The format is simple and professional. Tab-separated values. No fancy formatting. Just clean data.

**Format:**
- First row: Header row starting with the word "SUSPECT" in the top-left cell, followed by all member names (tab-separated)
- Remaining rows: One row per sender, starting with their name, then showing average amounts to each receiver
- Use the **full name** (e.g., "Pam Beesly", "Jim Halpert")
- Sort **alphabetically by the full name as a single string** (e.g., "Angela Martin" comes before "Dwight Schrute" which comes before "Jim Halpert")
- Use **tabs** (`\t`) to separate columns
- Show averages with **2 decimal places** (e.g., 1500.00)
- If no transactions occurred between two people, show **0.00**
- Include ALL 100 members (IDs 0-99), not just the gang members from Part 1

**Example output:**
```
SUSPECT	Angela Martin	Dwight Schrute	Jim Halpert	Pam Beesly
Angela Martin	0.00	300.00	0.00	0.00
Dwight Schrute	0.00	0.00	0.00	600.00
Jim Halpert	1200.00	0.00	0.00	1500.00
Pam Beesly	0.00	500.00	0.00	0.00
```

**Read this carefully:**
- The first column of the first row contains the word **"SUSPECT"**
- First row shows full names of members sorted alphabetically (starting after the word SUSPECT)
- First column shows full names of members sorted alphabetically (starting after the word SUSPECT)
- Each cell shows the average amount that **the row member (sender) sent to the column member (receiver)**
- Example: The cell at row "Jim Halpert" and column "Pam Beesly" shows the average amount Jim sent to Pam
- All 100 members must appear in both rows AND columns, in the same order

---

**CRITICAL RULES:**

- Include ALL 100 members (IDs 0-99) in your matrix
- When calculating averages: sum up all money sent from Person A to Person B, then divide by the number of transactions
- If Person A never sent money to Person B, show 0.00
- Sort alphabetically by full name (e.g., "Angela Martin" < "Dwight Schrute" < "Jim Halpert")
- Use **tabs** between columns (not spaces)
- Format all amounts with exactly 2 decimal places
- The top-left cell (row and column index 0,0) must contain the word "SUSPECT"

---

## 🔐 TECHNICAL REQUIREMENTS

Since Part 1 is complete and this case has been escalated to federal court, you are now **AUTHORIZED** to use advanced forensic tools that were previously restricted:

**YOU MAY NOW USE:**
- ✓ Dictionaries
- ✓ Lambda functions
- ✓ The `sorted()` function

**STILL PROHIBITED:**
- ✗ External libraries (Pandas, NumPy, CSV module, etc.) - we're in Scranton, not Silicon Valley
- ✗ Regular expressions
- ✗ Exception handling
- ✗ Comprehensions and generators
- ✗ Hardcoding any names or IDs - everything must be calculated from the data files

---

## 📋 DELIVERABLES

Python script called **enter_the_matrix.py** that generates **the_matrix.txt** in the exact format specified.

**The output file must be tab-separated with:**
- Header row: "SUSPECT" followed by all 100 member names (sorted alphabetically by full name)
- 100 data rows: One per member (sorted alphabetically by complete name), each containing their name followed by 100 average amounts
- Average amounts with exactly 2 decimal places
- 0.00 for pairs with no transactions

---

## ⚠️ IMPORTANT

**DO:**
- Include ALL 100 members (not just gang members from Part 1)
- Double-check your average calculations (sum ÷ count)
- Verify name sorting is correct (alphabetically by complete name string)
- Test your tab separation (copy-paste into Excel to verify it creates proper columns)
- Make sure all 100 members appear in both rows AND columns
- Use exactly 2 decimal places for all amounts
- Put "SUSPECT" in the top-left cell

---

## 📊 EVALUATION CRITERIA

This is federal evidence, Assistant. Either it's correct or it's not.
There is no partial credit in criminal court. The evidence either holds up or it doesn't.

---

## 🎯 FINAL NOTES

This matrix will be Exhibit A in the prosecution's case. When I present this to the jury, I need them to look at it and see the COMPLETE picture - not just the gang we identified, but everyone in this operation.

Some of these 100 members might be innocent. Some might be small-time. But the DA wants to see EVERYONE and how they're connected. That's how we build a complete case.

The beauty of this format is its simplicity. No fancy charts, no confusing graphics - just clean, organized data that shows exactly who was doing business with whom and for how much.

Make it perfect, Assistant. Defense attorneys will scrutinize every number. Prosecutors will rely on this to make their case. 

This is advanced forensic accounting. Show me you're ready for federal-level investigation work.

---

**Dwight K. Schrute III**  
Special Agent / Assistant Regional Manager  
Volunteer Sheriff Deputy  
Scranton Federal Task Force  

---
