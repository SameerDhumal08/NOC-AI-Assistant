"""
Creates and seeds the SQLite database with sample NOC resolved tickets.

Run:
python data/seed_noc_tickets.py
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "noc_tickets.db")

TICKETS = [

("INC000001","Linux","CPU Utilization High","CPU utilization crossed 95% on Linux application server APP-LNX-01.","Backup process was consuming high CPU. Restarted backup service. CPU utilization reduced to 32%.","Resolved"),

("INC000002","Linux","Memory Utilization High","Memory utilization reached 92% on APP-LNX-02.","Java application consuming excessive memory. Restarted Java service. Memory reduced to 58%.","Resolved"),

("INC000003","Linux","Disk Utilization High","Filesystem /var reached 91% utilization.","Removed old log files and temporary files. Disk usage reduced to 60%.","Resolved"),

("INC000004","Network","Port Down","Interface GigabitEthernet0/1 on Cisco Switch SW-HO-01 went down.","Cable found disconnected. Reconnected cable. Interface came UP.","Resolved"),

("INC000005","Network","Link Flapping","Router interface Gi0/0 showing continuous up/down events.","Faulty SFP module replaced. Link stabilized.","Resolved"),

("INC000006","Windows","Windows Service Down","IIS Service stopped unexpectedly on WEB-WIN-01.","Restarted IIS service and verified website accessibility.","Resolved"),

("INC000007","Database","Oracle Listener Down","Oracle listener not responding on DB-PRD-01.","Restarted Oracle listener using lsnrctl start. Database connectivity restored.","Resolved"),

("INC000008","Firewall","Firewall Interface Down","Outside interface on Palo Alto firewall became unavailable.","Interface reset completed. Connectivity restored.","Resolved"),

("INC000009","Monitoring","SNMP Down","Monitoring server unable to collect SNMP data from Router RTR-DR-01.","SNMP service restarted and community string corrected.","Resolved"),

("INC000010","Infrastructure","Server Down","Windows server not reachable from monitoring.","VM was powered off unexpectedly. Powered ON from VMware console.","Resolved"),

("INC000011","Linux","Swap Memory High","Swap utilization exceeded 80%.","Restarted memory-intensive application. Swap utilization reduced.","Resolved"),

("INC000012","Database","Tablespace Full","Oracle USERS tablespace reached 98%.","Added new datafile and extended tablespace.","Resolved"),

("INC000013","Windows","Disk Space Full","C Drive utilization exceeded 95%.","Deleted temporary files and archived logs.","Resolved"),

("INC000014","Network","High Network Latency","WAN latency increased above SLA.","ISP routing issue identified and resolved.","Resolved"),

("INC000015","Linux","Filesystem Read Only","Filesystem automatically remounted as read-only.","Performed filesystem check during maintenance and remounted filesystem.","Resolved"),

("INC000016","Security","SSL Certificate Expiry","SSL certificate expired on web application.","Installed renewed SSL certificate and restarted web server.","Resolved"),

("INC000017","Application","Application Down","Finance application inaccessible to users.","Restarted application service and validated user login.","Resolved"),

("INC000018","VMware","VM Snapshot Alert","Snapshot older than 30 days detected.","Deleted obsolete snapshot after approval.","Resolved"),

("INC000019","Active Directory","Domain Controller Replication Failed","AD replication failed between DC01 and DC02.","Restarted replication service and forced synchronization.","Resolved"),

("INC000020","Backup","Backup Failure","Nightly backup job failed.","Storage path unavailable. Storage mounted and backup rerun successfully.","Resolved")

]


def seed():

    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS tickets")

    cur.execute("""
       CREATE TABLE tickets (

       id INTEGER PRIMARY KEY AUTOINCREMENT,

       ticket_id TEXT,

       category TEXT,

       issue_type TEXT,

       description TEXT,

       resolution TEXT,

       status TEXT

       )
            """)

    cur.executemany(

        """
        INSERT INTO tickets
        (ticket_id, category, issue_type, description, resolution, status)

        VALUES (?,?,?,?,?,?)
        """,

        TICKETS

    )

    conn.commit()

    conn.close()

    print(f"Seeded {len(TICKETS)} NOC tickets into {DB_PATH}")


if __name__ == "__main__":
    seed()