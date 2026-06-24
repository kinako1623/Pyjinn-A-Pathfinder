from system.lib import minescript
import java, ast, time, math

pathfinder = java.import_pyjinn_script("mining/smooth_path.pyj")

path = pathfinder.get("goto")(-22, 71, -375).get()

minescript.echo(path)
raw_route_str = str(path)
new_route = ast.literal_eval(raw_route_str)

for x, y, z in new_route:
    minescript.execute(f"setblock {x} {y - 1} {z} minecraft:glowstone")

while True:
        status = pathfinder.get("move_status")
        if status == "arrived":
            print("exit 0")
            break
        elif status == "failed":
            print("exit 1")
            break
        time.sleep(0.1)
