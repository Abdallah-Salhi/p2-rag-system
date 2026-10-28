# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 259 (the final check needs at least 200)
- Words: 375,546
- Estimated tokens (words times 1.4): 525,764 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `if10288` | 1,522 | - | - | - |
| `if10382` | 1,662 | - | - | - |
| `if10397` | 1,051 | - | - | - |
| `if10479` | 1,788 | - | - | - |
| `if10519` | 1,684 | - | - | - |
| `if10521` | 1,700 | - | - | - |
| `if10589` | 1,092 | - | - | - |
| `if10639` | 1,571 | - | - | - |
| `if10668` | 1,803 | - | - | - |
| `if10752` | 1,618 | - | - | - |
| `if10753` | 1,438 | - | - | - |
| `if10762` | 878 | - | - | - |
| `if10763` | 1,765 | - | - | - |
| `if10778` | 1,502 | - | - | - |
| `if10799` | 1,749 | - | - | - |
| `if10819` | 1,801 | - | - | - |
| `if10842` | 1,751 | - | - | - |
| `if10844` | 1,388 | - | - | - |
| `if10857` | 1,493 | - | - | - |
| `if10869` | 1,865 | - | - | - |
| `if10904` | 1,456 | - | - | - |
| `if10927` | 1,309 | - | - | - |
| `if10941` | 1,580 | - | - | - |
| `if10945` | 1,903 | - | - | - |
| `if10979` | 1,333 | - | - | - |
| `if11017` | 1,684 | - | - | - |
| `if11027` | 1,841 | - | - | - |
| `if11036` | 1,542 | - | - | - |
| `if11050` | 1,688 | - | - | - |
| `if11095` | 2,006 | - | - | - |
| `if11103` | 1,741 | - | - | - |
| `if11138` | 1,633 | - | - | - |
| `if11156` | 1,690 | - | - | - |
| `if11177` | 1,640 | - | - | - |
| `if11183` | 1,657 | - | - | - |
| `if11201` | 1,062 | - | - | - |
| `if11257` | 1,507 | - | - | - |
| `if11299` | 1,508 | - | - | - |
| `if11307` | 1,549 | - | - | - |
| `if11316` | 1,370 | - | - | - |
| `if11331` | 1,666 | - | - | - |
| `if11345` | 1,388 | - | - | - |
| `if11354` | 1,509 | - | - | - |
| `if11404` | 1,232 | - | - | - |
| `if11431` | 1,430 | - | - | - |
| `if11446` | 1,272 | - | - | - |
| `if11453` | 1,543 | - | - | - |
| `if11455` | 1,379 | - | - | - |
| `if11476` | 1,698 | - | - | - |
| `if11501` | 1,605 | - | - | - |
| `if11514` | 1,609 | - | - | - |
| `if11541` | 1,756 | - | - | - |
| `if11628` | 1,724 | - | - | - |
| `if11639` | 1,792 | - | - | - |
| `if11649` | 1,421 | - | - | - |
| `if11691` | 1,628 | - | - | - |
| `if11693` | 1,514 | - | - | - |
| `if11696` | 1,761 | - | - | - |
| `if11697` | 1,568 | - | - | - |
| `if11746` | 1,724 | - | - | - |
| `if11754` | 1,497 | - | - | - |
| `if11779` | 1,453 | - | - | - |
| `if11785` | 1,434 | - | - | - |
| `if11791` | 1,223 | - | - | - |
| `if11793` | 1,584 | - | - | - |
| `if11815` | 1,357 | - | - | - |
| `if11821` | 995 | - | - | - |
| `if11827` | 1,432 | - | - | - |
| `if11844` | 1,721 | - | - | - |
| `if11861` | 1,545 | - | - | - |
| `if11878` | 1,589 | - | - | - |
| `if11909` | 1,892 | - | - | - |
| `if11921` | 1,619 | - | - | - |
| `if11999` | 1,529 | - | - | - |
| `if12036` | 1,143 | - | - | - |
| `if12043` | 1,295 | - | - | - |
| `if12072` | 1,881 | - | - | - |
| `if12108` | 1,735 | - | - | - |
| `if12161` | 1,552 | - | - | - |
| `if12163` | 1,571 | - | - | - |
| `if12178` | 1,741 | - | - | - |
| `if12238` | 1,298 | - | - | - |
| `if12253` | 1,481 | - | - | - |
| `if12258` | 1,652 | - | - | - |
| `if12273` | 1,186 | - | - | - |
| `if12282` | 1,773 | - | - | - |
| `if12286` | 1,656 | - | - | - |
| `if12288` | 1,494 | - | - | - |
| `if12290` | 1,763 | - | - | - |
| `if12300` | 1,577 | - | - | - |
| `if12307` | 1,704 | - | - | - |
| `if12324` | 1,642 | - | - | - |
| `if12387` | 1,593 | - | - | - |
| `if12411` | 1,816 | - | - | - |
| `if12413` | 1,993 | - | - | - |
| `if12433` | 1,877 | - | - | - |
| `if12439` | 1,471 | - | - | - |
| `if12448` | 1,472 | - | - | - |
| `if12459` | 1,667 | - | - | - |
| `if12487` | 1,688 | - | - | - |
| `if12491` | 1,928 | - | - | - |
| `if12502` | 1,734 | - | - | - |
| `if12526` | 1,422 | - | - | - |
| `if12602` | 1,430 | - | - | - |
| `if12603` | 1,705 | - | - | - |
| `if12650` | 1,767 | - | - | - |
| `if12652` | 1,233 | - | - | - |
| `if12684` | 1,431 | - | - | - |
| `if12692` | 1,134 | - | - | - |
| `if12707` | 1,811 | - | - | - |
| `if12733` | 1,096 | - | - | - |
| `if12748` | 1,577 | - | - | - |
| `if12753` | 1,727 | - | - | - |
| `if12757` | 1,773 | - | - | - |
| `if12819` | 1,927 | - | - | - |
| `if12841` | 1,871 | - | - | - |
| `if12862` | 1,722 | - | - | - |
| `if12913` | 2,052 | - | - | - |
| `if12916` | 1,849 | - | - | - |
| `if12971` | 1,022 | - | - | - |
| `if12991` | 1,748 | - | - | - |
| `if13034` | 1,696 | - | - | - |
| `if13052` | 1,531 | - | - | - |
| `if13064` | 1,791 | - | - | - |
| `if13089` | 1,824 | - | - | - |
| `if13119` | 2,306 | - | - | - |
| `if13157` | 1,503 | - | - | - |
| `if13159` | 1,942 | - | - | - |
| `if13211` | 1,080 | - | - | - |
| `if13223` | 1,587 | - | - | - |
| `if13278` | 1,703 | - | - | - |
| `if13331` | 1,792 | - | - | - |
| `ig10043` | 170 | - | - | - |
| `ig10046` | 306 | - | - | - |
| `ig10052` | 164 | - | - | - |
| `ig10058` | 157 | - | - | - |
| `ig10076` | 296 | - | - | - |
| `in10731` | 1,157 | - | - | - |
| `in10856` | 1,051 | - | - | - |
| `in10864` | 987 | - | - | - |
| `in10866` | 1,078 | - | - | - |
| `in10873` | 900 | - | - | - |
| `in10895` | 983 | - | - | - |
| `in10930` | 967 | - | - | - |
| `in10942` | 968 | - | - | - |
| `in11060` | 943 | - | - | - |
| `in11065` | 964 | - | - | - |
| `in11131` | 876 | - | - | - |
| `in11142` | 947 | - | - | - |
| `in11149` | 970 | - | - | - |
| `in11162` | 946 | - | - | - |
| `in11174` | 986 | - | - | - |
| `in11189` | 986 | - | - | - |
| `in11242` | 997 | - | - | - |
| `in11300` | 1,011 | - | - | - |
| `in11353` | 1,089 | - | - | - |
| `in11373` | 1,085 | - | - | - |
| `in11380` | 1,073 | - | - | - |
| `in11412` | 1,121 | - | - | - |
| `in11432` | 1,005 | - | - | - |
| `in11445` | 1,046 | - | - | - |
| `in11452` | 1,079 | - | - | - |
| `in11468` | 1,035 | - | - | - |
| `in11545` | 1,123 | - | - | - |
| `in11559` | 1,110 | - | - | - |
| `in11598` | 1,108 | - | - | - |
| `in11601` | 1,052 | - | - | - |
| `in11633` | 1,022 | - | - | - |
| `in11648` | 928 | - | - | - |
| `in11654` | 1,180 | - | - | - |
| `in11666` | 1,060 | - | - | - |
| `in11667` | 1,057 | - | - | - |
| `in11683` | 1,134 | - | - | - |
| `in11696` | 1,095 | - | - | - |
| `in11710` | 877 | - | - | - |
| `in11727` | 959 | - | - | - |
| `in11798` | 1,041 | - | - | - |
| `in11821` | 1,053 | - | - | - |
| `in11828` | 1,127 | - | - | - |
| `in11883` | 972 | - | - | - |
| `in11884` | 1,013 | - | - | - |
| `in11900` | 1,070 | - | - | - |
| `in11916` | 1,048 | - | - | - |
| `in11943` | 1,056 | - | - | - |
| `in11944` | 1,059 | - | - | - |
| `in11946` | 1,718 | - | - | - |
| `in11964` | 1,049 | - | - | - |
| `in11972` | 1,048 | - | - | - |
| `in11978` | 1,099 | - | - | - |
| `in11980` | 1,190 | - | - | - |
| `in11981` | 1,117 | - | - | - |
| `in11983` | 1,146 | - | - | - |
| `in11984` | 962 | - | - | - |
| `in12006` | 981 | - | - | - |
| `in12011` | 1,127 | - | - | - |
| `in12032` | 1,014 | - | - | - |
| `in12048` | 1,060 | - | - | - |
| `in12051` | 1,020 | - | - | - |
| `in12071` | 1,191 | - | - | - |
| `in12074` | 1,098 | - | - | - |
| `in12082` | 1,063 | - | - | - |
| `in12090` | 1,129 | - | - | - |
| `in12096` | 903 | - | - | - |
| `in12110` | 942 | - | - | - |
| `in12161` | 1,051 | - | - | - |
| `in12169` | 1,106 | - | - | - |
| `in12179` | 1,031 | - | - | - |
| `in12250` | 876 | - | - | - |
| `in12269` | 1,035 | - | - | - |
| `in12279` | 882 | - | - | - |
| `in12288` | 1,075 | - | - | - |
| `in12334` | 1,075 | - | - | - |
| `in12412` | 1,119 | - | - | - |
| `in12422` | 1,380 | - | - | - |
| `in12423` | 1,424 | - | - | - |
| `in12464` | 1,166 | - | - | - |
| `in12465` | 1,161 | - | - | - |
| `in12488` | 1,191 | - | - | - |
| `in12528` | 1,008 | - | - | - |
| `in12542` | 1,000 | - | - | - |
| `in12557` | 1,029 | - | - | - |
| `in12575` | 970 | - | - | - |
| `in12611` | 891 | - | - | - |
| `in12717` | 1,030 | - | - | - |
| `in12719` | 2,003 | - | - | - |
| `in12746` | 971 | - | - | - |
| `lsb10065` | 1,111 | - | - | - |
| `lsb10066` | 1,690 | - | - | - |
| `lsb10198` | 1,668 | - | - | - |
| `lsb10199` | 1,278 | - | - | - |
| `lsb10281` | 2,150 | - | - | - |
| `lsb10289` | 1,351 | - | - | - |
| `lsb10325` | 2,406 | - | - | - |
| `lsb10359` | 1,464 | - | - | - |
| `lsb10418` | 1,800 | - | - | - |
| `lsb10457` | 1,834 | - | - | - |
| `lsb10503` | 1,393 | - | - | - |
| `lsb10585` | 1,510 | - | - | - |
| `lsb10605` | 2,581 | - | - | - |
| `lsb10622` | 2,667 | - | - | - |
| `lsb10634` | 1,514 | - | - | - |
| `lsb10666` | 2,798 | - | - | - |
| `lsb10736` | 2,505 | - | - | - |
| `lsb10791` | 2,962 | - | - | - |
| `lsb10805` | 2,705 | - | - | - |
| `lsb11010` | 1,824 | - | - | - |
| `lsb11054` | 1,803 | - | - | - |
| `lsb11199` | 3,262 | - | - | - |
| `lsb11259` | 1,366 | - | - | - |
| `lsb11296` | 2,214 | - | - | - |
| `lsb11320` | 2,756 | - | - | - |
| `lsb11333` | 2,831 | - | - | - |
| `lsb11372` | 1,876 | - | - | - |
| `lsb11385` | 3,925 | - | - | - |
| `lsb11388` | 1,336 | - | - | - |
| `lsb11402` | 2,091 | - | - | - |
| `lsb11453` | 1,864 | - | - | - |
| `lsb11461` | 2,500 | - | - | - |
| `lsb11478` | 1,645 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
