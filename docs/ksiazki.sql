/* kategorie */

INSERT INTO `django`.`books_categories` (`id`, `name`) VALUES (NULL, 'Fantastyka');
INSERT INTO `django`.`books_categories` (`id`, `name`) VALUES (NULL, 'Informatyka');
INSERT INTO `django`.`books_categories` (`id`, `name`) VALUES (NULL, 'Nauka języków');
INSERT INTO `django`.`books_categories` (`id`, `name`) VALUES (NULL, 'Sensacja, kryminał');

/* książki */

/****************** 1 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Oko jelenia. Tom 7. Sowie zwierciadło', '

Długo wyczekiwana siódma część wielotomowej powieści fantastycznej Andrzeja Pilipiuka! Gratka dla największych fanów przygód Marka Oberecha, Staszka i Heleny Korzyckiej!

To bardzo złe miejsce i bardzo zły czas. Jesień 1864 roku. Rzucony tu Staszek musi uratować dziewczynę, a przy okazji zmienić bieg historii. Historii, której zmienić się przecież nie da, a nieświadomy chłopak już na początku pozbawia życia ośmiu uzbrojonych Rosjan. Co dalej?

Jak zwykle masa przygód, którym bieg nadają wciąż chętne tak do bitki, jak i upitki grupy awanturniczych młodzieńców czekających w swoich dworach. To właśnie przez nie wiedzie fabuła "Sowiego zwierciadła". Od folwarku pod Rejowcem, aż po Lublin przez kraj objęty okupacją. Przez jarmarki, salony, kamienice, wsie, lasy i pola. Tam gdzie leje się krew, a walka jest przegrana. Na pewno?
', 'Pilipiuk Andrzej', 'Fabryka Słów Sp. z o.o.', '35.49', '32', '2015-05-01 00:00:00', '1', '2514639875124', '1');

/****************** 2 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Pieśń Lodu i Ognia. Tom 4. Uczta dla wron. Część 2. Sieć spisków', '

Wojna pięciu królów zbliża się powoli do końca, a Lannisterowie i ich sojusznicy uważają się za zwycięzców, jednakże nie wszystko w kraju idzie dobrze. To czas, gdy mądrzy i ambitni, podstępni i silni, zdobędą umiejętności, siłę i magiczne talenty potrzebne, by przeżyć straszliwy okres, jaki ich oczekuje. Czas, w którym szlachetnie urodzeni i prości ludzie, żołnierze i czarodzieje, skrytobójcy i mędrcy muszą połączyć siły, ponieważ na uczcie dla wron jest wielu gości, ale tylko nieliczni ujdą z niej z życiem.
', 'George R. R. Martin', 'Wydawnictwo Zysk i S-ka', '52.99', '15', '2015-05-02 00:00:00', '0', '5698322561429', '1');

/****************** 3 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Kłamca. Papież sztuk', '

Jubileusz bestsellerowego cyklu!

To już dziesięć lat od kiedy pierwszy tom Kłamcy zagościł na półkach i w sercach czytelników.

Loki – nordycki bóg kłamstwa na usługach aniołów, a także, mimochodem, bohater pięciu książek, komiksu i gry karcianej – nie ma czasu świętować. Oto bowiem przyjdzie mu się zmierzyć z jednym z największych swoich wrogów. W dodatku na własne życzenie, bo wszystko wskazuje na to, że Dezyderiusza Crane’a, samozwańczego boga popkultury, stworzył omyłkowo nie kto inny jak Loki właśnie.

Teraz rozpoczyna się gra z czasem, tym trudniejsza, że z każdą chwilą nowy bóg coraz lepiej poznaje swoje możliwości. Jego główną mocą jest kontrola nad narracją, a nawet... nad całą opowieścią.

Jubileuszowa powieść o Lokim to wariacka jazda bez trzymanki umiejscowiona fabularnie pomiędzy opowiadaniami z drugiego tomu. Pełna gościnnych występów, ciętych bon-motów i będących wyznacznikiem serii popkulturowych nawiązań usatysfakcjonuje wszystkich miłośników Kłamcy.
', 'Ćwiek Jakub', 'Wydawnictwo SQN', '30.99', '3', '2015-05-03 00:00:00', '1', '2547865325984', '1');

/****************** 4 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Vademecum Walkenbacha. Zaawansowane wykorzystanie Excela. Analizy Business Intelligence', '

Poznaj potencjał Excela w zakresie BI!

Program Excel można stosować na setki różnych sposobów, chociaż większość użytkowników uważa go za prosty arkusz kalkulacyjny. Co więcej, wachlarz jego zaawansowanych funkcjonalności jest stale poszerzany — program stał się częścią pakietu Microsoft Business Intelligence. Dzięki możliwości integracji danych z różnych źródeł Excel świetnie sprawdza się jako narzędzie do tworzenia interaktywnych kokpitów menedżerskich. Jeżeli interesujesz się tematyką BI i masz ambicję stworzyć własne „centrum dowodzenia”, to trzymasz w rękach właściwą książkę!

Ten wspaniały podręcznik stanowi kompendium wiedzy na temat prowadzenia analiz BI w środowisku Microsoft Excel. Sięgnij po niego i sprawdź, jak korzystać z tabel przestawnych oraz narzędzi Power Pivot, Power View czy Power Map. Dowiedz się, jak do tego wszystkiego dołożyć dane z baz SQL oraz użyć dodatku Data Mining. Zdobądź też wiedzę na temat publikowania twoich rozwiązań na stronach SharePoint. Książka ta jest obowiązkową lekturą dla wszystkich menedżerów i analityków biznesowych chcących mieć wgląd w bieżące dane. Gdy poznasz i zastosujesz narzędzia Excela, podjęcie właściwej decyzji stanie się łatwiejsze!
', 'Alexander Michael', 'Wydawnictwo Helion', '61.99', '2', '2015-05-04 00:00:00', '0', '5698475144426', '2');

/****************** 5 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'JavaScript i jQuery. Interaktywne strony WWW dla każdego', '

JavaScript to język, który w dużej mierze ukształtował współczesne strony WWW. Dzięki niemu możemy swobodnie korzystać z interaktywnych, wygodnych w użyciu oraz niezawodnych aplikacji internetowych. Pojawienie się JavaScriptu pozwoliło zastąpić tradycyjne aplikacje desktopowe nowymi, pracującymi w chmurze. Wokół języka powstało już wiele narzędzi i bibliotek. Jedną z najpopularniejszych jest jQuery.

Jeżeli chcesz poznać potencjał tego duetu i zacząć tworzyć atrakcyjne aplikacje internetowe, nie możesz obejść się bez tej książki. Pomoże Ci ona szybko stworzyć pierwszy skrypt. W trakcie lektury poznasz niuanse składni JavaScriptu, sposoby obsługi zdarzeń oraz obiektowy model strony. Dzięki dalszym rozdziałom zdobędziesz wiedzę na temat jQuery oraz możliwości tej biblioteki. Z pomocą duetu JavaScript i jQuery błyskawicznie rozwiążesz każdy problem — asynchroniczne pobieranie danych z serwera, atrakcyjny interfejs użytkownika, zaawansowana obsługa formularzy to tylko niektóre z poruszanych tu tematów. Książka ta jest doskonałym źródłem informacji dla czytelników chcących opanować JavaScript oraz związane z nim narzędzia!
', 'Duckett Jon', 'Wydawnictwo Helion', '88.99', '2', '2015-05-05 00:00:00', '1', '2688955564124', '2');

/****************** 6 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Język C++', '

Oto nowe wydanie - znacznie rozszerzone - najlepszego w świecie podręcznika C++, napisanego przez twórcę tego języka. Każdy student informatyki i każdy programista powinien je mieć. Uwzględniono w nim ostateczną wersję standardu ANSI/ISO C++. Opisano język, jego bibliotekę standardową i podstawowe metody projektowania w ujęciu całościowym. Jest to pełen wykład z programowania obiektowego.
', 'Stroustrup Bjarne', 'Wydawnictwa Naukowo-Techniczne', '116.99', '7', '2015-05-06 00:00:00', '0', '5896565986698', '2');

/****************** 7 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Python. Programuj szybko i wydajnie', '

Python to skryptowy język programowania istniejący na rynku od wielu lat — jego pierwsza wersja pojawiła się w 1991 roku. Przejrzystość kodu źródłowego była jednym z głównych celów Guida van Rossuma, twórcy tego języka. Dziś Python cieszy się dużą popularnością, co z jednej strony świadczy o jego przydatności, a z drugiej gwarantuje użytkownikom szerokie wsparcie społeczności programistów języka. Python jest elastyczny, dopuszcza różne style programowania, a dzięki temu znajduje zastosowanie w wielu miejscach świata IT.

Jeżeli chcesz w pełni wykorzystać możliwości Pythona i tworzyć wydajne rozwiązania, to koniecznie zaopatrz się w tę książkę! Dzięki niej dowiesz się, jak wykorzystać profilowanie do lokalizowania „wąskich gardeł”, oraz poznasz efektywne techniki wyszukiwania danych na listach, w słownikach i zbiorach.

Ponadto zdobędziesz wiedzę na temat obliczeń macierzowych i wektorowych oraz zobaczysz, jak kompilacja do postaci kodu C wpływa na wydajność twojego rozwiązania. Osobne rozdziały zostały poświęcone współbieżności oraz modułowi multiprocessing. Opanowanie tych zagadnień pozwoli ci ogromnie przyspieszyć działanie Twojej aplikacji. Na sam koniec nauczysz się tworzyć klastry i kolejki zadań oraz optymalizować zużycie pamięci RAM. Rozdział dwunasty to gratka dla wszystkich — zawiera najlepsze porady specjalistów z branży!

Książka ta jest obowiązkową lekturą dla wszystkich programistów chcących tworzyć wydajne rozwiązania w języku Python.
', 'Gorelick Micha', 'Wydawnictwo Helion', '46.99', '212', '2015-05-07 00:00:00', '0', '1565598653256', '2');

/****************** 8 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Angielski w 1 miesiąc. Ekstrapakiet', '

Ekstrapakiet "w 1 miesiąc" to doskonały pomysł na naukę języka obcego dla początkujących. Dzięki zawartemu w nimi kursowi z książką i podręcznikiem, szybko przyswoisz sobie podstawy języka oraz gruntownie poznasz język w zakresie, umożliwiającym codzienną komunikację.

Poprzez liczne przykłady nauczysz się, co powiedzieć w określonych sytuacjach. Poznasz podstawy gramatyki, objaśnianej po polsku, a najważniejsze informacje o niej znajdziesz w dodatkowej, 12 stronicowej, poręcznej wkładce, którą możesz wpiąć do segregatora.

Całość kursu dostępna jest również w postaci książki elektronicznej, dostępnej w sieci po wpisaniu kodu, znajdującego się w pakiecie.
', 'Opracowanie zbiorowe', 'Wydawnictwo LektorKlett', '31.49', '212', '2015-05-08 00:00:00', '1', '5666699865323', '3');

/****************** 9 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Cztery Żywioły. Tom 2. Okularnik', '

Kontynuacja bestsellerowego "Pochłaniacza" z Saszą Załuską w roli głównej. Drugi tom serii "Cztery Żywioły" Katarzyny Bondy!

Nie ma ciała, nie ma zbrodni. Tak przynajmniej może wydawać się każdemu, kto otarł się choćby w najmniejszym stopniu o policyjną pracę, do której zamierza w końcu powrócić Sasza Załuska. Jeszcze tylko do końca uporządkuje swoje osobiste sprawy, rozprawi się na zawsze z przeszłością i znów stanie się profilerką.

Podczas krótkiego urlopu w podlaskiej Hajnówce bierze udział w tradycyjnym białoruskim weselu. To właśnie tam dochodzi do uprowadzenia panny młodej, która, jak potem się okazuje, nie jest pierwszą zaginioną kobietą. W okolicznych lasach wciąż znajdowane są ludzkie szczątki i wydawałoby się, że nic nie łączy tych spraw. Nic, poza okularnikiem - starym mercedesem, który zawsze pojawia się w pobliżu.

W tym samym czasie na jaw wychodzi mroczna przeszłość mieszkańców podlaskiej wsi, a straszne tajemnice sięgają jeszcze czasów II wojny światowej.

Co tak naprawdę sprawiło, że sielski urlop zamienił się w powikłane śledztwo z masą krwawych wątków, które wcale nie są ze sobą spójne?
', 'Bonda Katarzyna', 'Wydawnictwo MUZA S.A.', '35.49', '3', '2015-05-09 00:00:00', '0', '5984556989963', '4');

/****************** 10 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Niemowa', '

W domu w Torsby zostają zamordowani członkowie rodziny Carsltenów ‒ matka, ojciec i dwoje dzieci. Wszyscy zginęli od strzałów oddanych z bliska.  Wkrótce po makabrycznym odkryciu na miejscu zjawia się Sebastian Bergman wraz z resztą ekipy z Krajowej Policji Kryminalnej.

Śledztwo jest skomplikowane, a napięcie  wzrasta, kiedy jedyny podejrzany ginie zastrzelony z tej samej broni co Carsltenowie.

Detektywi odkrywają, że świadkiem morderstwa rodziny była dziesięcioletnia Nicole. Policja musi odnaleźć dziewczynkę, zanim… zrobi to morderca.
', 'Hjorth Michael', 'Czarna Owca dawniej Jacek Santorski & Co.', '34.99', '11', '2015-05-10 00:00:00', '0', '1265945214255', '4');

/****************** 11 ******************/

INSERT INTO `django`.`books_book` (`id`, `title`, `description`, `author`, `publisher`, `price`, `quantity`, `date_added`, `sale`, `isbn`, `category_id`) VALUES (NULL, 'Umarli mają głos. Prawdziwe historie', '

Poznaj krwawą historię współczesnej Polski – zbrodnie w afekcie i szczegółowo zaplanowane morderstwa, seksualne dewiacje i rytualne mordy. Obgryziona do połowy ręka. Ciemnożółta masa wylewająca się z worka na zwłoki. Larwy ścierwicy i fetor rozkładającego się ciała.

Tak prowadzi się śledztwo w zimnym świetle prosektorium.
', 'Krajewski Marek, Kawecki Jerzy', 'Społeczny Instytut Wydawniczy Znak', '30.99', '45', '2015-05-11 00:00:00', '1', '2656998956471', '4');
