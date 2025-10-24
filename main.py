from alarm import Alarm

import time
from monitor import hämta_cpu_anvandning, hämta_minnesanvändning, hämta_diskanvändning
larm_lista = []


def starta_övervakningslage():
    print("\n🔍 Övervakningsläge startat.")
    print("Tryck Ctrl + C för att avbryta och återgå till huvudmenyn.\n")

    try:
        while True:
            cpu = hämta_cpu_användning()
            mem_procent, _, _ = hämta_minnesanvändning()
            disk_procent, _, _ = hämta_diskanvändning()

            print("Systemet övervakas...")

            for alarm in larm_lista:
                if alarm.är_aktiverat(cpu, mem_procent, disk_procent):
                    print(
                        f"⚠️  VARNING: {alarm.typ}-användning överstiger {alarm.nivå}%")

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nAvbröt övervakningsläge. Återgår till huvudmenyn...")

    except KeyboardInterrupt:
        print("\nAvbröt övervakningsläge. Återgår till huvudmenyn...")


def visa_larm():
    print("\n-- Aktiva larm --")

    if not larm_lista:
        print("Inga larm har konfigurerats ännu.")
    else:
        # Sortera listan på typ av larm (funktionell programmering!)
        sorterade = sorted(larm_lista, key=lambda alarm: alarm.typ)

        for alarm in sorterade:
            print(alarm)

    input("\nTryck ENTER för att gå tillbaka till huvudmenyn...")


def skapa_larm():
    print("\n-- Skapa ett larm --")
    print("1. CPU-användning")
    print("2. Minnesanvändning")
    print("3. Diskanvändning")
    print("0. Tillbaka till huvudmeny")

    val = input("Välj ett område att sätta larm på: ")

    if val == "0":
        return

    if val not in ["1", "2", "3"]:
        print("Felaktigt val. Försök igen.")
        return

    try:
        nivå = int(input("Ställ in nivå för larm (1-100): "))
        if nivå < 1 or nivå > 100:
            print("Du måste skriva en siffra mellan 1 och 100.")
            return
    except ValueError:
        print("Du måste skriva en siffra!")
        return

    if val == "1":
        larm_typ = "CPU"
    elif val == "2":
        larm_typ = "Minne"
    else:
        larm_typ = "Disk"

    larm_lista.append(Alarm(larm_typ, nivå))

    print(f"Larm för {larm_typ} satt till {nivå}%")


def huvudmeny():
    while True:
        print("\n--- Systemövervakningsapplikation ---")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")

        val = input("Välj ett alternativ: ")

        if val == "1":
            print("Startar övervakning... (inte implementerat ännu)")
        elif val == "2":
            visa_overvakning()
        elif val == "3":
            skapa_larm()
        elif val == "4":
            visa_larm()
        elif val == "5":
            starta_overvakningslage()
        elif val == "0":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")


def visa_övervakning():
    cpu = hämta_cpu_användning()
    mem_procent, mem_anvant, mem_total = hämta_minnesanvändning()
    disk_procent, disk_anvant, disk_total = hämta_diskanvändning()

    print(f"\nCPU Användning: {cpu}%")
    print(
        f"Minnesanvändning: {mem_procent}% ({mem_anvant} GB av {mem_total} GB)")
    print(
        f"Diskanvändning: {disk_procent}% ({disk_anvant} GB av {disk_total} GB)")

    input("\nTryck enter för att gå tillbaka till huvudmenyn...")


# Starta programmet
huvudmeny()

