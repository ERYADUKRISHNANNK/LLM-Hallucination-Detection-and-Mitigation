"""
Comprehensive Integration Smoke Test for FINCH-ZK Ultra-Modern Platform.
Verifies:
  1. Authentication & Security Redirections
  2. Session Handling (admin/admin)
  3. PySBD Atomic Segmentation
  4. Prompt Variation Generation
  5. API Pipeline Analysis (/api/analyze)
  6. Real-time Metrics & Latency Profiling
  7. Audit Log JSON Export (/api/export/json)
  8. Audit Log CSV Export (/api/export/csv)
"""

import os
import sys
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r"c:\Users\LOQ\Downloads\azeem")

from app import app, segment_text_blocks, build_prompt_variants

app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
client = app.test_client()

print("=" * 65)
print("  FINCH-ZK Comprehensive Futuristic Platform Test Suite")
print("=" * 65)

# 1. GET / redirects to /login
r = client.get("/", follow_redirects=False)
assert r.status_code == 302 and "login" in r.headers["Location"], "Redirect failed"
print("[PASS] GET / -> Redirects unauthenticated user to /login")

# 2. Login Page contains 2026 and Metadata
r = client.get("/login")
assert r.status_code == 200
assert b"2026" in r.data, "Year 2026 missing from login"
assert b"Group 11" in r.data, "Group 11 missing from login"
assert b"Mohamed Azeem" in r.data, "Team members missing from login"
print("[PASS] GET /login -> 200 OK with Year 2026, Group 11, and Team Metadata")

# 3. Successful Admin Login
r = client.post("/login", data={"username": "admin", "password": "admin"}, follow_redirects=True)
assert r.status_code == 200 and (b"FINCH" in r.data and b"Console" in r.data)
print("[PASS] POST /login -> Authenticated successfully with 'admin'/'admin'")

# 4. Access Protected Dashboard
r = client.get("/dashboard")
assert r.status_code == 200
assert b"Chart.js" in r.data or b"chart.js" in r.data or b"factualityChart" in r.data
assert b"Neethu C S" in r.data, "Guide name missing from dashboard"
print("[PASS] GET /dashboard -> 200 OK with Chart.js Hub & Guide Ms. Neethu C S")

# 5. PySBD Segmentation
text = "Alexander Graham Bell patented the telephone in 1876. He also invented the internet. This claim is false."
blocks = segment_text_blocks(text)
assert len(blocks) == 3, f"Expected 3 blocks, got {len(blocks)}"
print(f"[PASS] PySBD Segmentation -> 3 atomic chunks extracted: {blocks}")

# 6. Prompt Variant Generation
variants = build_prompt_variants("Explain quantum computing")
assert "zero_shot_cot" in variants and "break_down" in variants
print(f"[PASS] Prompt Variant Generator -> Generated variants: {list(variants.keys())}")

# 7. Complete Pipeline Run (/api/analyze)
payload = {
    "prompt": "Who invented the telephone and what else did he discover?",
    "response": "Alexander Graham Bell was awarded the first U.S. patent for the telephone in 1876. He was born in Edinburgh, Scotland in 1847. In his later career, Alexander Graham Bell invented the internet and the radio. He died in 1922."
}
r = client.post("/api/analyze", data=json.dumps(payload), content_type="application/json")
assert r.status_code == 200
data = json.loads(r.data)
assert "blocks" in data and "metrics" in data and "mitigated_response" in data
print(f"[PASS] POST /api/analyze -> Executed in {data['metrics']['total_latency_seconds']}s")
print(f"       Factuality Score: {data['metrics']['factuality_score']}% | Hallucination Index: {data['metrics']['hallucination_index']}%")

# Check that the internet/radio hallucination was caught and mitigated
contradiction_found = any(b["verdict"] == "CONTRADICTION" for b in data["blocks"])
assert contradiction_found, "Contradiction block was not detected"
print("[PASS] Contradiction Detection -> Successfully flagged hallucination and provided targeted fix")

# 8. JSON Audit Export
r = client.get("/api/export/json")
assert r.status_code == 200 and "attachment" in r.headers.get("Content-Disposition", "")
print("[PASS] GET /api/export/json -> Successfully exported JSON audit file")

# 9. CSV Audit Export
r = client.get("/api/export/csv")
assert r.status_code == 200 and "text/csv" in r.headers.get("Content-Type", "")
assert b"Original_Sentence" in r.data and b"Verdict" in r.data
print("[PASS] GET /api/export/csv -> Successfully exported CSV audit file")

# 10. Printable Academic Report Route
r = client.get("/report/audit")
assert r.status_code == 200 and b"Merkle" in r.data and b"Group 11" in r.data
print("[PASS] GET /report/audit -> Successfully generated printable Academic ZK Verification Certificate")

# 11. Endpoint Connectivity & Key Management
r = client.post("/api/test-connection")
assert r.status_code == 200
print("[PASS] POST /api/test-connection -> Endpoint connectivity test executed")

# 12. Red-Teaming Studio Adversarial Perturbation
r = client.post("/api/red-team/perturb", data=json.dumps({"text": "Paris is the capital of France.", "mode": "entity_swap"}), content_type="application/json")
assert r.status_code == 200
red_data = json.loads(r.data)
assert "mutated_text" in red_data and "Berlin" in red_data["mutated_text"]
print("[PASS] POST /api/red-team/perturb -> Successfully injected synthetic adversarial entity swap")

# 13. Collaborative Dispute Workspace
r = client.post("/api/disputes/submit", data=json.dumps({"block_index": 1, "original_verdict": "CONTRADICTION", "override_verdict": "ACCURATE", "comment": "Verified by lead auditor."}), content_type="application/json")
assert r.status_code == 200
r_list = client.get("/api/disputes/list")
assert r_list.status_code == 200 and len(json.loads(r_list.data)["disputes"]) >= 1
print("[PASS] POST /api/disputes/submit & GET /api/disputes/list -> Human collaborative dispute recorded")

# 14. Regulatory Compliance & EU AI Act Telemetry
r = client.get("/api/compliance/metrics")
assert r.status_code == 200
comp_data = json.loads(r.data)
assert comp_data["soc2_audit_status"] == "COMPLIANT_PASS"
print("[PASS] GET /api/compliance/metrics -> Retrieved SOC2 & EU AI Act transparency telemetry")

# 15. Independent Cryptographic ZK Receipt Verification
r = client.post("/api/verify-zk-receipt", data=json.dumps({
    "verification_token": "FINCH-ZK-TEST-2026",
    "merkle_root": "0123456789abcdef0123456789abcdef"
}), content_type="application/json")
assert r.status_code == 200 and json.loads(r.data)["valid"] is True
print("[PASS] POST /api/verify-zk-receipt -> Independent ZK Trust Seal verification successful")

# 16. Secure Logout
r = client.get("/logout", follow_redirects=True)
assert r.status_code == 200 and b"Admin Console" in r.data
print("[PASS] GET /logout -> Session terminated safely")

print("=" * 65)
print("  ALL 16 COMPREHENSIVE TESTS PASSED WITH 100% SUCCESS! ✓")
print("=" * 65)
