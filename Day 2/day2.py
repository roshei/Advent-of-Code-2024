def isSafe(report):
    levels = list(map(int, report.split()))
    
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    isMonotonic = increasing or decreasing
    
    validDifferences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    
    return isMonotonic and validDifferences

def isSafeWithDampener(report):
    if isSafe(report):
        return True
    
    levels = report.split()
    for i in range(len(levels)):
        modified_report = " ".join(levels[:i] + levels[i + 1:])
        if isSafe(modified_report):
            return True
    
    return False

def countSafeReports(reports):
    with open(reports, 'r') as file:
        data = file.readlines()
    
    return sum(1 for report in data if isSafe(report.strip()))

def countSafeWithDampener(reports):
    with open(reports, 'r') as file:
        data = file.readlines()
        
    return sum(1 for report in data if report.strip() and isSafeWithDampener(report.strip()))

reports = r"C:\Users\Roni\Advent-of-Code-2024\Day 2\reports.txt"

safeReports = countSafeReports(reports)
safeWithDampener = countSafeWithDampener(reports)

print(f"Safe reports: {safeReports}")
print(f"Safe with dampener {safeWithDampener}")