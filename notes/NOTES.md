# Interpretation von Markdown

Wenn ein Element nicht in einem eigenen Abschnitt steht, wird es zum vorherigen interpretiert. Ein paragraph beginnt immer mit einer Leerzeile und eine Leerzeile erzeugt das beginnen mit einem neuen Element.


# Grundlegender Ablauf

1. Lies das Dokument ein
2. Zerteile es an den Leerzeilen.
3. Für jedes Element Identifiziere seinen Typ
4. Erzeuge ein neues Element des Typs und hänge es an die Outputliste an

# Aufbau

Die Klasse MarkdownKonvert stellt das zentrale element dar. Dieses erstellt das Markdown Objekt und den Writer. Der Writer bekommt das MarkdownKonvert Objekt als parent mit.
Das Rendern des Templates wird vom MarkdownKonvert Objekt eingeleitet.

Das Kommandozeileninterface wird mittels docopt implementiert.

# Reguläre Ausdrücke:

Gruppen werden in Headings immer durch () erzeugt. Gruppe 0 ist das gesammte Match objekt   

Headings: r"(^ {0,3}#{1,4} ?)([0-9].*?[A-Z].*)"
