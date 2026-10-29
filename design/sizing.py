"""One quintal sizing for the hollow cylinder paddy dryer. Estimates, not tests."""

def main():
    m_i = 100.0
    M_i = 0.22
    M_f = 0.14
    m_w = m_i * (M_i - M_f) / (1.0 - M_f)
    dry = m_i * (1.0 - M_i)
    final = dry / (1.0 - M_f)
    rho_b = 560.0
    V = m_i / rho_b
    L = 0.60
    A = V / L
    print("batch_kg", m_i)
    print("water_removed_kg", round(m_w, 2))
    print("dry_solid_kg", round(dry, 2))
    print("final_grain_kg", round(final, 2))
    print("bed_volume_m3", round(V, 3))
    print("annulus_area_m2", round(A, 3))
    print("first_trial_air_C", "40 to 45")
    print("grain_limit_C", 50)
    print("alternate_blower_air_C", 80)
    print("status", "estimate, not a measured plant")

if __name__ == "__main__":
    main()
