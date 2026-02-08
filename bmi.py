# bmi.py
# Complete compute_bmi.
# Do not change parse_people or the __main__ test harness.

def read_lines(path):
    """
    Lazily yields lines from a UTF-8 text file, without trailing newline.
    If the file can't be opened, yield a single line:
       'ERROR: cannot open file'
    Use: try/except + with-open + yield
    """ 
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                yield line.rstrip("\n")
    except OSError:
        yield "ERROR: cannot open file"
    


# --- Provided: parses and validates basic fields (do not modify) ---
def parse_people(lines):
    """
    lines: an iterable of raw lines (from read_lines)
    Yields (line_no, record_dict) for valid data rows.
    Skips empty lines. Expects exact header:
        name,age,height_cm,weight_kg
    Prints readable error messages with line numbers on bad rows.

    record_dict keys: 'name', 'age', 'height_cm', 'weight_kg'
    """
    header = None
    expected = ["name", "age", "height_cm", "weight_kg"]

    for idx, raw in enumerate(lines, start=1):          # enumerate used here
        if not raw.strip():
            continue

        # Handle file-open error line: pass through as a single message and stop
        if raw.startswith("ERROR:"):
            print(raw)
            return

        if header is None:
            cols = [c.strip() for c in raw.split(",")]
            if cols != expected:
                print(f"Header error: expected {expected}, got {cols}")
                return
            header = cols
            continue

        parts = [p.strip() for p in raw.split(",")]
        if len(parts) != 4:
            print(f"Line {idx}: wrong number of fields ({len(parts)})")
            continue

        # Map columns to values via zip (zip used here)
        record = dict(zip(header, parts))
        try:
            record["age"] = int(record["age"])
            record["height_cm"] = float(record["height_cm"])
            record["weight_kg"] = float(record["weight_kg"])
        except ValueError:
            print(
                f"Line {idx}: invalid numeric fields -> "
                f"age='{record['age']}', height='{record['height_cm']}', weight='{record['weight_kg']}'"
            )
            continue

        yield idx, record


# --- Task 1 (You complete) ---
def compute_bmi(parsed_records):
    """
    parsed_records: an iterable of (line_no, record_dict) from parse_people
    Generator: for each valid record, yield (line_no, name, bmi)

    BMI = weight_kg / (height_m ** 2), height_m = height_cm / 100
    - Round BMI to 1 decimal place (round(..., 1))
    - If height is <= 0, print: f"Line {line_no}: non-positive height {height_cm}"
      and skip the row.
    - Use 'zip' at least once in any simple, meaningful way. Examples:
        * zip((weight,), (height_m**2,)) to pair numerator/denominator
        * OR build a formatted debug pair: list(zip(("name","bmi"), (name, bmi)))
    - Use 'yield' to return results one by one
    """
    # TODO: your code here

    for index, record in parsed_records:
        name=record["name"]
        weight=record["weight_kg"]
        height=record["height_cm"]/100
    
        if height <= 0:
            print(f"Line {index}: non-positive height {height}")
            continue
        
        try:
            bmi=round(weight/(height**2),1)
            
        except:
            print (record)
            continue
        
        yield index,name,bmi
            
        
        
        
            
               
               
    

def main(path):
    lines = read_lines(path)
    parsed = parse_people(lines)
    for i, (line_no, name, bmi) in enumerate(compute_bmi(parsed), start=1):
        print(f"{i}. {name}: BMI {bmi}")
        if i == 5:  # only show first 5 for demo
            break

if __name__ == "__main__":
    
    main("./Assignments/bmi.txt")
