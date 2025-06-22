# Factory Method Pattern Implementation
from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFExporter(ReportExporter):
    def export(self, data):
        print(f"Exporting report as PDF: {data}")
        return f"PDF report generated"

class CSVExporter(ReportExporter):
    def export(self, data):
        print(f"Exporting report as CSV: {data}")
        return f"CSV report generated"

class JSONExporter(ReportExporter):
    def export(self, data):
        print(f"Exporting report as JSON: {data}")
        return f"JSON report generated"

class ExporterFactory:
    @staticmethod
    def get_exporter(format_type):
        if format_type == "pdf":
            return PDFExporter()
        elif format_type == "csv":
            return CSVExporter()
        elif format_type == "json":
            return JSONExporter()
        else:
            raise ValueError(f"Unsupported format: {format_type}")

# Example usage
if __name__ == "__main__":
    factory = ExporterFactory()
    exporter = factory.get_exporter("pdf")
    result = exporter.export({"name": "Pavan", "marks": 100})
    print(result)
