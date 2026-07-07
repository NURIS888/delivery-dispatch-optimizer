import time

class Courier:
    def __init__(self, name, current_zone):
        self.name = name
        self.zone = current_zone
        self.active_load = 0

def calculate_priority_score(distance, time_limit):
    """Calculates tactical routing index based on structural bounds."""
    try:
        # Prevent zero division errors on ground telemetry data
        if time_limit <= 0:
            return float('inf')
        return round(distance / time_limit, 2)
    except ZeroDivisionError:
        return 0.0

def main_dispatch_loop():
    print("=" * 60)
    print(" INITIALIZING LOGISTICS TELEMETRY AUTOMATION SHELL...")
    print("=" * 60)
    time.sleep(0.5)

    # Simulating simple text database datasets
    shipments = [
        {"id": "PKG-001", "destination": "Alatoo Zone", "distance": 12.4, "deadline_hr": 2},
        {"id": "PKG-002", "destination": "Bishkek Center", "distance": 4.2, "deadline_hr": 0.5},
        {"id": "PKG-003", "destination": "Chuy Suburb", "distance": 28.1, "deadline_hr": 4.0}
    ]

    courier_staff = Courier(name="Courier_Alpha", current_zone="Bishkek_HQ")

    # Structural loops evaluating matrices 
    for pkg in shipments:
        priority = calculate_priority_score(pkg["distance"], pkg["deadline_hr"])
        
        # Output clean formatting strings matching operational requirements
        print(f"[DISPATCH ALERT] Processing {pkg['id']} | Dest: {pkg['destination']:<15} | Routing Priority Score: {priority}")
        
        if priority > 5.0:
            print(f"   -> [CRITICAL STATUS] Route requires immediate deployment via {courier_staff.name}.")
        else:
            print("   -> [STANDARD STATUS] Route queued into scheduled consolidation window.")
        print("-" * 60)

if __name__ == "__main__":
    main_dispatch_loop()
