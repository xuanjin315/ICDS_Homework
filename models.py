class Record:
    def __init__(self, name: str):
        # TODO: store the name
        if not isinstance(name,str):
            return TypeError("name must be a string")
        self.name=name

    def summary_line(self) -> str:
        """
        Abstract method: should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must override summary_line()")


class ErrorRecord(Record):
    def __init__(self, name: str, reason: str):
        # TODO: call superclass constructor and store reason
        if not isinstance(name,str) or not isinstance(name,str):
            raise TypeError("name and reason must be str")
        self.name=name
        self.reason=reason

    def summary_line(self) -> str:
        # TODO: return formatted string like: "name=... | ERROR: ..."
        return f"name={self.name}|ERROR:{self.reason}"


class BMIMetricRecord(Record):
    def __init__(self, name: str, height_cm: float, weight_kg: float):
        # TODO: call superclass constructor and store height and weight
        if not isinstance(name,str):
            raise TypeError("name must be a str")
        if not isinstance(height_cm, float) or not isinstance(weight_kg,float):
            raise TypeError("height_cm and weight_kg must be float")
        self.name=name
        self.height=height_cm
        self.weight=weight_kg

    def bmi(self) -> float:
       
        self.BMI = round(self.weight / (self.height/100)**2,1)
       
        # TODO: implement BMI calculation
        

    def summary_line(self) -> str:
        # TODO: return formatted string like: "name=... | BMI: ..."
        return f"name={self.name}|BMI:{self.BMI}"