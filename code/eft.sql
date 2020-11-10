create table Classes(
    c_class varchar(32) PRIMARY KEY,
    c_total integer,
    c_num integer
);

create table Ammunition(
    a_caliber varchar(32),
    a_ammuntion varchar(32)
);

create table Weapons(
    w_class integer,
    weapon_name varchar(32),
    firing_mode varchar(32),
    fire_rate varchar(32),
    caliber integer
);

create table Armor(
    arm_class integer,
    arm_class integer,
    arm_zones varchar(32),
    durability integer,
    movment_speed integer,
    turn_speed integer,
    ergo integer
);

create table Backpack(
    b_class integer,
    b_name varchar(32),
    b_innerGrid varchar(32),
    b_outerGrid varchar(32),
    b_totalSlots integer,
    b_storageEfficiency integer,
    b_weight intger
);

create table GearMods(
    g_class integer,
    g_name varchar(32),
    g_recoil integer,
    g_ergo integer
);

create table VitalParts(
    v_class integer,
    v_name varchar(32),
    v_recoil integer,
    v_accuracy integer,
    v_muzzleVelocity integer
);

create table Sights(
    s_class integer,
    s_name varchar(32),
    s_recoil integer,
    s_ergo integer,
    s_accuracy integer,
    s_sightingRange integer,
    s_magnification varchar(32),
);

create table Magazine(
    m_name varchar(32),
    m_recoil integer,
    m_ergo integer,
    m_checkSpeed integer,
    m_loadSpeed integer,
    m_capacity varchar(32)
);

