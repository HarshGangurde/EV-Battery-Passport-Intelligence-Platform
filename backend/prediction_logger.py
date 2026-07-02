from db import get_connection
from datetime import datetime


def log_prediction(
    vehicle_id,
    battery_type,
    total_distance,
    charging_time,
    predicted_soh,
    degradation,
    estimated_soc,
    anomaly_warning,
    risk_rating,
    model_version="Student-v1"
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_logs(

            prediction_time,
            vehicle_id,
            battery_type,
            total_distance,
            charging_time,
            predicted_soh,
            degradation,
            estimated_soc,
            anomaly_warning,
            risk_rating,
            model_version

        )

        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,

        (
            datetime.now(),
            vehicle_id,
            battery_type,
            total_distance,
            charging_time,
            predicted_soh,
            degradation,
            estimated_soc,
            bool(anomaly_warning),
            risk_rating,
            model_version
        )
    )

    conn.commit()

    cursor.close()
    conn.close()