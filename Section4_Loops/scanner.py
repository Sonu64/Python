# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    # Write your code below this line
    result = []
    for code in parcel_codes:
        if code == "DAMAGED":
            result.append("Skipped damaged parcel")
            continue
        elif code == "STOP":
            result.append("Critical error: Stopping scan")
            break
        result.append(f"Scanned parcel: {code}")
    else:
        result.append("All parcels scanned successfully")
    return result
    pass

print(scan_parcels(["DAMAGED", "STOP", "9834899"]))