from db import get_connection
import time

def init_db():
    retries = 10
    while retries > 0:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicle(
                user_id VARCHAR(255),
                vehicle_id VARCHAR(255) PRIMARY KEY,
                battery_type VARCHAR(100),
                buying_price FLOAT,
                buying_date DATE,
                manufacture_date DATE
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS prediction_logs(
            id SERIAL PRIMARY KEY,
            prediction_time TIMESTAMP,
            vehicle_id VARCHAR(255),
            battery_type VARCHAR(100),
            total_distance FLOAT,
            charging_time FLOAT,
            predicted_soh FLOAT,
            degradation FLOAT,
            estimated_soc FLOAT,
            anomaly_warning BOOLEAN,
            risk_rating VARCHAR(50),
            model_version VARCHAR(50))""")
            
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ PostgreSQL Connected")
            return

        except Exception as e:

            print(f"Database not ready... Retrying ({retries})")
            print(e)
            retries -= 1
            time.sleep(3)
    raise Exception("Unable to connect to PostgreSQL")