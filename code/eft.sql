-- Q1: Print entire Classes table
select * 
from Classes;

-- Q2: Print all Sub-Classes, types, and the total number of items
select Class, Type as Subclass, SubClass_Weapons.Total as Total
from Classes, SubClass_Weapons
where Classes.Class_Number = SubClass_Weapons.Class_Number
union
select Class, Type as Subclass, SubClass_Wearables.Total as Total
from Classes, SubClass_Wearables
where Classes.Class_Number = SubClass_Wearables.Class_Number
union
select Class, Type as Subclass, SubClass_WeaponModifications.Total as Total
from Classes, SubClass_WeaponModifications
where Classes.Class_Number = SubClass_WeaponModifications.Class_Number
union
select Class, Type as Subclass, SubClass_Health_Buffs.Total as Total
from Classes, SubClass_Health_Buffs
where Classes.Class_Number = SubClass_Health_Buffs.Class_Number;

-- Q3: Print all weapons under the Assualt Rifle class
select Name as 'Assault Rifles'
from Weapons, SubClass_Weapons
where Weapons.SC_Number = SubClass_Weapons.SC_number AND
        SubClass_Weapons.SC_number = 1;

-- Q4: Print total number of ammo types per weapon; order by totAmmo_types descending
select Weapons.Name as 'Weapon Name', count(Ammunition.name) as 'Total # of Ammo Types'
from Weapons, Ammunition
where Weapons.Caliber = Ammunition.Caliber
group by Weapons.Name
order by 'Total # of Ammo Types' desc;

-- Q5: Print all backpack having greater than 20 inventory slots
select Name as 'Backpack Name', slots as 'Inventory Space'
from Backpacks
group by Name
having slots > 20;

-- Q6: Print all armors that do not protect the thorax and stomach
select Name as 'Armor Name', armorZones as Protects
from 'Armor Vest'
where Protects <> 'Thorax and Stomach';

-- Q7: Print the average fire rate of each weapon class
select SubClass_Weapons.Type as 'Weapon Type', avg(FireRate) as 'Average Fire Rate'
from SubClass_Weapons, Weapons
where SubClass_Weapons.SC_number = Weapons.SC_Number
group by SubClass_Weapons.Type;

-- Q8: Print all health items that remove fracture and are of type 'Light Bleeding'
select Name as 'Health Item', effect as Effect
from Health
where Type = 'Injury Treatment' AND
        effect LIKE '%Light Bleeding%';

-- Q9: Print all Classes that can be sold by the NPC_Traders
-- Why is it printing every class for every trader?
select NPC_Traders.Nickname as Trader, group_concat(Classes.Class, ', ') as Tradeables
from NPC_Traders, Classes
where Trader = 'Therapist' AND
        Tradeables IN (select npc.Tradeables
                        from NPC_Traders npc 
                        where npc.Tradeables LIKE '%1%' OR
                                npc.Tradeables LIKE '%2%' OR
                                npc.Tradeables LIKE '%3%' OR
                                npc.Tradeables LIKE '%4%')
group by Trader;

-- Q10: Print all gear mods that produce recoil; order in ascending order
select Name as 'Gear Mods', recoil as Recoil
from 'Gear Mods'
where Recoil <> 0
order by Recoil asc;

-- Q11: Print all attachments specifically for the AK-74
select distinct Name as Attachments, Type
from 'Gear Mods' gm, SubClass_WeaponModifications
where gm.SC_Number = SubClass_WeaponModifications.SC_Number AND
        Name LIKE '%AK-74%'
group by Attachments
union 
select distinct Name as Attachments, Type
from 'Vital Parts' vp, SubClass_WeaponModifications
where vp.SC_Number = SubClass_WeaponModifications.SC_Number AND
        Name LIKE '%AK-74%'
group by Attachments
union
select distinct Name as Attachments, Type
from Sights, SubClass_WeaponModifications
where Sights.SC_Number = SubClass_WeaponModifications.SC_Number AND
        Name LIKE '%AK-74%'
group by Attachments
union 
select distinct Magazines.Name as Attachments, Type
from Magazines, Weapons, SubClass_WeaponModifications
where Magazines.Caliber = Weapons.Caliber AND
        Magazines.SC_Number = SubClass_WeaponModifications.SC_Number AND
        Weapons.Name = '%AK-74%'
group by Attachments;

-- Q12: Print all magazines (and their capacity and caliber) except the 12x70 mm caliber
select Name as Magazines, capacity, Caliber
from Magazines
except 
select Name as Magazines, capacity, Caliber
from Magazines 
where Caliber LIKE '%12x70 mm%';

-- Q13: Print all health items with useTime between 2-3 that remove heavy bleeding 
Select Name, Type, effect, useTime
from Health
where useTime between 2 and 3 AND
        effect LIKE '%Removes:%' AND
        effect LIKE '%Heavy Bleeding%';

-- Q14: Print all information regarding Weapons, Magazines, and Ammunition at caliber = 7.62x25 mm
select Weapons.Name as Weapons, Magazines.Name as Magazines, Ammunition.Name as Ammunition
from ((Weapons
inner join Magazines on Weapons.Caliber = Magazines.Caliber)
inner join Ammunition on Weapons.Caliber = Ammunition.Caliber) 
where Weapons.Caliber = '7.62x25 mm';

-- Q15: Print the name of all wearables
select Name as Wearables, Type
from 'Armor Vest' av, SubClass_Wearables
where av.SC_Number = SubClass_Wearables.SC_Number
union all
select Name as Wearables, Type
from Backpacks, SubClass_Wearables
where Backpacks.SC_Number = SubClass_Wearables.SC_Number;

-- Q16: Print the armor vest with the greatest and least durabilty
select Name as 'Armor Vest', penType as 'Pen Type', armorZones as 'Armor Zones', max(Durability) as Durability,
        movementspeed as 'Movement Speed', turnSpeed as 'Turn Speed', ergonomics as Ergonomics
from 'Armor Vest'
union 
select Name as 'Armor Vest', penType as 'Pen Type', armorZones as 'Armor Zones', min(Durability) as Durability,
        movementspeed as 'Movement Speed', turnSpeed as 'Turn Speed', ergonomics as Ergonomics
from 'Armor Vest';

-- Q17: Print the average sighting range of sights with magnification vs sights without magnification
select avg(s1.range) as 'Average Range: Magnified Sights', avg(s2.range) as 'Average Range: non-Magnified Sights'
from Sights s1, Sights s2 
where s1.magnification <> 0 AND
        s2.magnification = 0;

-- Q18: Print all vital parts who have a muzzle velocity that is non-zero and greater than the average of all non-zero muzzle velocities
--       order by muzzle velocity in descending order
select Name, recoil as Recoil, ergonomics as Ergonomics, accuracy as Accuracy, muzzleVelocity as 'Muzzle Velocity'
from 'Vital Parts' v1
where v1.muzzleVelocity <> 0 AND
        v1.muzzleVelocity > (select avg(v2.muzzleVelocity)
                            from 'Vital Parts' v2
                            where v2.muzzleVelocity <> 0)
order by v1.muzzleVelocity desc;

-- Q19: Print all attachments for each Assault Carbine
select distinct Weapons.Name as Weapon, group_concat(gm.Name, ', ') as 'Gear Mods', group_concat(vp.Name, ', ') as 'Vital Parts', group_concat(Sights.Name, ', ') as Sights, group_concat(Magazines.name, ', ') as Magazines
from SubClass_Weapons scw, Weapons, 'Gear Mods' gm , 'Vital Parts' vp, Sights, Magazines
where scw.SC_Number = Weapons.SC_Number AND 
        Weapons.Caliber = Magazines.Caliber AND 
        Weapons.SC_Number = 2 AND
        gm.Name IN (select distinct gm2.Name
                    from 'Gear Mods' gm2
                    where gm2.Name LIKE '%AS VAL%' OR
                            gm2.Name LIKE '%OP-SKS%' OR
                            gm2.Name LIKE '%SKS%' OR
                            gm2.Name LIKE '%Vepr Hunter/VP0-101%') AND
        vp.Name IN (select distinct vp2.Name
                    from 'Vital Parts' vp2
                    where vp2.Name LIKE '%AS VAL%' OR
                            vp2.Name LIKE '%OP-SKS%' OR
                            vp2.Name LIKE '%SKS%' OR
                            vp2.Name LIKE '%Vepr Hunter/VP0-101%') AND
        Sights.Name IN (select distinct s2.Name
                    from Sights s2
                    where s2.Name LIKE '%AS VAL%' OR
                            s2.Name LIKE '%OP-SKS%' OR
                            s2.Name LIKE '%SKS%' OR
                            s2.Name LIKE '%Vepr Hunter/VP0-101%')
group by Weapon;

-- Q20: Select all weapons that only have single fire mode 
select Name as Weapon, FireRate as 'Fire Rate'
from Weapons
where FiringModes = 'Single'
order by FireRate desc;