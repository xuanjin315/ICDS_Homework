from models import ErrorRecord, BMIMetricRecord


def read_lines(path):
    """
    Lazily yield non-empty, non-comment lines from a text file.
    """
    # TODO: open file and yield valid lines
    with open(path,"r",encoding="UTF-8") as f:
        for line in f:
            stripped_line=line.strip()
            if not stripped_line or stripped_line.startswith('#'):
                continue
            
            yield stripped_line



def parse_people(lines):
    """
    Parse raw lines into dictionaries with headers as keys.
    """
    # TODO: split header, iterate over lines, zip headers with values
    lines=iter(lines)
    try:
        header_line=next(lines)
    except StopIteration:
        return
    
    headers=header_line.split(",")
    for line_no,raw in enumerate(lines,start=2):
        data_line=raw.split(",")
        data=dict(zip(headers,data_line))
        yield {
            "line_no":line_no,
            "raw":raw,
            "data":data
               }

        
        
        
    


def build_records(parsed_records):
    """
    Convert parsed dictionaries into ErrorRecord or BMIMetricRecord objects.
    """
    # TODO: try to convert height and weight into floats
    # TODO: handle errors using ErrorRecord
    # TODO: return BMIMetricRecord for valid data
    for record in parsed_records:
        data=record["data"]
        name=data["name"]
        
        try:
            height_cm=float(data["height_cm"])
            weight_kg=float(data["weight_kg"])
            if height_cm<=0:
                raise ValueError("height_cm must be > 0")
            if weight_kg<=0:
                raise ValueError("weight_kg must be >0")
            
            output=BMIMetricRecord(name,height_cm,weight_kg)
            output.bmi()
            yield output
                
        except Exception as e:
            yield ErrorRecord(name,str(e))


def write_results(records, out_path):
    """
    Write summary lines of records into an output file.
    """
    # TODO: open file for writing and output each record's summary_line()
    with open(out_path,"w",encoding="UTF-8") as f:
        for record in records:
            f.write(record.summary_line()+"\n")


if __name__ == "__main__":
    in_path = "bmi.txt"
    out_path = "bmi_out.txt"

    lines = read_lines(in_path)
    parsed = parse_people(lines)
    records = build_records(parsed)
    write_results(records, out_path)