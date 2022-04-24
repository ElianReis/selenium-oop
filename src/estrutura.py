class Estrutura:
    def __init__(self):
        self.holandappiurl = "https://opendata.cbs.nl/statline/#/CBS/en/dataset/83936ENG/table?ts=1562272187018"

        self.holandacpiurl = "https://opendata.cbs.nl/statline/#/CBS/en/dataset/83131ENG/table?ts=1562269785328"

        self.austriahicpurl = (
            "https://www.oenb.at/isaweb/report.do;jsessionid=1120B8F1D833096ABDB3A68DAE8DA4B1"
            "?report=6.3 "
        )

        self.japaocpiurl = (
            "https://www.e-stat.go.jp/en/stat-search/files?page=1&layout=datalist&toukei=00200573"
            "&tstat=000001150147&cycle=1&tclass1=000001150149&cycle_facet=cycle&tclass2val=0 "
        )

        self.japaoppiurl = (
            "https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_s050_en"
        )

        self.japaoppi = [
            "body > div.contents > div > ul.tabContent > li > div.toggleBar.clearfix > div:nth-child(2) > form > div "
            "> input",
            ".searchCondtion .tableDataCodeHeader label",
            "#columnNameSearch",
        ]

        self.alemanhacpi = [".btn-prim .btn-flex-grid", "#os_zr_senden_de", "#CSV"]

        self.alemanhacpiurl = (
            "https://www-genesis.destatis.de/genesis//online?operation=table&code=61111-0002&bypass"
            "=true&levelindex=0&levelid=1643287989266#abreadcrumb "
        )

        self.austriahicp = [
            "#timeSeries_J",
            "#langen",
            "#mjVon > option:nth-child(24)",
            "#mmVon > option:nth-child(1)",
            "body > form:nth-child(7) > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > "
            "input",
            "body > form:nth-child(2) > table > tbody > tr > td.optionen > select > option:nth-child(1)",
            "body > form:nth-child(2) > table > tbody > tr > td:nth-child(3) > input",
        ]

        self.holandacpi = [
            ".rows .pvtAttrEditHandle",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > span > span.fancytree-checkbox.fa.fa-square",
            "#ts_modal > div > div > div.modal-header.ui-draggable-handle > button.fa.fa-check.close.apply",
            "#pivotTableOutput > table > thead > tr:nth-child(3) > th.pvtContainer > ul > li.axis_0 > "
            "span.pvtAttrEditHandle",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > ul > li:nth-child(5) > span > "
            "span.fancytree-checkbox.fa.fa-check-square-o",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > ul > li:nth-child(6) > span > "
            "span.fancytree-checkbox.fa.fa-check-square-o",
            "#ts_modal > div > div > div.modal-header.ui-draggable-handle > button.fa.fa-check.close.apply",
            ".fa-download",
            ".DownloadCSV",
        ]
        self.holandappi = [
            ".rows .pvtAttrEditHandle",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > span > span.fancytree-checkbox.fa.fa-square",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > span > "
            "span.fancytree-checkbox.fa.fa-check-square-o",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > ul > li:nth-child(1) > ul > li > ul > "
            "li:nth-child(2) > span > span.fancytree-checkbox.fa.fa-square-o",
            "#ts_modal > div > div > div.modal-header.ui-draggable-handle > button.fa.fa-check.close.apply",
            ".axis_2 .pvtAttrEditHandle",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > span > span.fancytree-checkbox.fa.fa-square",
            "#ts_modal > div > div > div.modal-header.ui-draggable-handle > button.fa.fa-check.close.apply",
            "#pivotTableOutput > table > thead > tr:nth-child(3) > th.pvtContainer > ul > li.axis_0 > "
            "span.pvtAttrEditHandle",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > ul > li:nth-child(2) > span > "
            "span.fancytree-checkbox.fa.fa-check-square-o",
            "#ts_modal > div > div > div.modal-body > div > div > ul > li > ul > li:nth-child(3) > span > "
            "span.fancytree-checkbox.fa.fa-check-square-o",
            "#ts_modal > div > div > div.modal-header.ui-draggable-handle > button.fa.fa-check.close.apply",
            ".fa-download",
            ".DownloadCSV",
        ]
        self.japaocpi = ['.stat-dataset_list-item:nth-child(1) .stat-download_icon_left .stat-dl_text']
