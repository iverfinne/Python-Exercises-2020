#Oppgave 6
def MinÅrligeInnbetaling(beløp, årlig_rente, løpetid_år):
    n = løpetid_år
    r = (årlig_rente / 100)
    årlig_beløp = (r * beløp * ((1+r) ** n)) / (((1+r) ** n) - 1)
    return årlig_beløp

løpetid_år = int(7)
årlig_rente = float(0.06)
beløp = int(600000)

print('Årlig innbetaling i NOK: {}'.format(MinÅrligeInnbetaling(beløp, årlig_rente, 
løpetid_år)))