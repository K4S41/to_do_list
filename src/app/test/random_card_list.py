from app.dto import CardList, Task, Label, Tag
from random import randint, choice
from typing import List
import json

label = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

tags = [
    "ProkrastinaceMistr",
    "MůjVnitřníChaos",
    "NevímKdeZačít",
    "OblíbenýÚkolNaprostoNepodstatný",
    "Předstírám,ŽePracuji",
    "NejsemJistý,CoToZnamená",
    "ZítřekJeNovýDen",
    "ChvilkaNaÚvahu",
    "UžZaseToSamé",
    "SkrytýPokladKonečnéhoDne",
]

items = [
    "Vymyslet nové jméno pro vaši domácí rostlinu a s ním se bavit celý den.",
    "Pokusit se naučit pár nových tanců a předvést je svým domácím mazlíčkům.",
    "Udělat si sraz s přáteli online a soutěžit v tom, kdo umí vytvořit nejlepší rýmovanou básni o brokolici.",
    "Postavit pevnost z polštářů a dek a hrát si na odolávání invazi plyšových medvídků.",
    "Udělat si filmový večer s filmy, které jste naposledy viděli, když jste byli malí.",
    "Zkusit napodobit zvuky zvířat a hádat, které zvíře to je.",
    "Vytvořit nový recept na 'neviditelný dort' a pozvat přátele na ochutnávku.",
    "Vytvořit seznam neobvyklých věcí, které chcete udělat, alespoň jednou za život.",
    "Vymyslet příběh o vašem každodenním dobrodružství jako by byl vyprávěn hrdinou fantasy příběhu.",
    "Vytvořit plakát s názvem 'Ztracené a nalezené' pro všechny vaše ztracené ponožky.",
    'Zkusit naučit svého domácího mazlíčka nový trik a vytvořit z něj videohodiny.',
    'Udělat si falešnou reklamu na svůj imaginární produkt a sdílet ji na sociálních sítích.',
    'Zorganizovat vlastní "ples pod dekou" s hudbou a světelnými efekty ve vaší obývací místnosti.',
    'Vytvořit seznam deseti vtipných věcí, které můžete udělat s použitím pouze věcí, které máte v kuchyni.',
    'Vymyslet "tajnou identitu" a hrát si na skrytého agenta po zbytek dne.',
    'Vyfotit selfie s každým předmětem ve vašem domě a vytvořit "výletní album" z vaší každodenní rutiny.',
    'Zkusit namalovat portrét svého domácího mazlíčka, i když jste nikdy předtím nekreslili.',
    'Procházet svou knihovnu a najít knihy s nejzábavnějšími názvy a citovat je na Twitteru.',
    'Vytvořit vlastní "návod na přežití" pro něco absurdního, jako je například "Jak přežít invazi mimozemšťanů s použitím pouze pásku a mikrovlnky".',
    'Připravit si vlastní "karaoke večer" s přáteli prostřednictvím videokonference.',
    'Zkusit naučit se základní fráze ve fiktivním jazyce a používat je v běžných situacích.',
    'Organizovat "schůzku se sebou samým" a udělat si večer jen pro sebe.',
    'Vytvořit seznam nejzvláštnějších věcí, které jste viděli na internetu tento týden.',
    'Udělat si čas na "hodinu smíchu" a sledovat komediální seriály nebo stand-up speciály.',
    'Vytvořit vlastní parodický blog o svých každodenních zážitcích.',
    'Zorganizovat si "denní tanec ve sprše" a vytvořit si svůj vlastní playlist s písničkami.',
    'Zkusit se naučit novou dovednost online prostřednictvím bezplatných kurzů.',
    'Udělat si "hodinu kreativity" a vyrobit něco nového z předmětů, které máte doma.',
    'Vymyslet fiktivní postavu a psát deníkové zápisy z jejího života.',
    'Sepsat seznam nejlepších vtipů, které jste slyšeli, a podělit se o ně s přáteli.',
]

titles = [
    "Jednodenní únik do zapomenutí",
    "Šťastné smutky: Průvodce smíchem a slzami",
    "Když je pes vaším jediným poradcem",
    "Tajemství zapomenutých kočičích dobrodružství",
    "Všední den v časopise nevšedního života",
    "Díky štěstí: Průvodce nečekanými výhrami a prohrami",
    "Zmatení a úzkost: Deník moderního klauna",
    "Dočasně ztracený: Příběh objevování sama sebe",
    "Ve stínu osamělosti: Průvodce jedinými stíny na zdi",
]


class RandomCardList:
    def __init__(self):
        self.start_id = randint(1, 1000)

    def get_id(self) -> int:
        self.start_id += 1
        return self.start_id

    def get_label(self) -> Label:
        return Label(color=choice(label))

    def get_tag(self) -> Tag:
        return Tag(text=choice(tags))

    def get_task(self) -> Task:
        return Task(
            id=self.get_id(),
            item=choice(items),
            labels=[self.get_label() for _ in range(randint(0, 2))],
            tags=[self.get_tag() for _ in range(randint(0, 2))],
        )

    def get_card_list(self) -> list[CardList]:
        return [
            CardList(
                id=index,
                title=choice(titles),
                cards=[self.get_task() for _ in range(randint(5, 10))],
            )
            for index in range(1, randint(5, 10))
        ]
