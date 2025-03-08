from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.master_data import MasterData
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    *,
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["payroll_accounting_month"] = payroll_accounting_month

    params["payroll_accounting_month_end"] = payroll_accounting_month_end

    params["payroll_recalculation_month"] = payroll_recalculation_month

    params["payroll_recalculation_month_end"] = payroll_recalculation_month_end


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/employees/masterdata".format(client_id=client_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = MasterData.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400
    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())



        return response_404
    if response.status_code == 500:
        response_500 = ErrorMessage5Xx.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    """ Get the list of employees' masterdata

     Masterdata of all employees can be accessed by the client's client-id.



     If a non-mandatory field is not filled in the payroll system, the field will not be exported
    through the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **sex**   |  Lodas: 0 = männlich, 1 = weiblich, 2 = divers, 3 = unbestimmt  |
    |           |  Lohn und Gehalt: 0 = weiblich, 1 = männlich, 2 = divers, 3 = unbestimmt |
    | **denomination/spouses_denomination**  |  Lodas:  0 = Konfessionslos / Keine
    Kirchensteuerberechnung, 1 = ev - Evangelische Kirchensteuer, 2 = rk - Römisch-Katholische
    Kirchensteuer, 3 = ak - Altkatholische Kirchensteuer, 4 = fa - Freie Religionsgemeinschaft Alzey, 5
    = fb - Freireligiöse Landesgemeinde Baden, 6 = fg - Freireligiöse Landesgemeinde Pfalz, 7 = fm -
    Freireligiöse Gemeinde Mainz, 8 = fr - Französisch reformiert (bis 12/2015), 9 = fs - Freireligiöse
    Gemeinde Offenbach/Main, 10 = ib - Israelitische Religionsgemeinschaft Baden, 11 = ih - Jüdische
    Kultussteuer, 12 = il - Israelitische Kultussteuer der kultusberechtigten Gemeinden, 13 = is -
    Israelitische / Jüdische Kultussteuer, 14 = iw - Israelitische Religionsgemeinschaft Württembergs,
    15 = jd - Jüdische Kultussteuer, 16 = jh - Jüdische Kultussteuer, 17 = lt - Evangelisch lutherisch
    (bis 12/2015), 18 = rf - Evangelisch reformiert (bis 12/2015) |
    |                    |  Lohn und Gehalt:  00 = Konfessionslos / Keine Kirchensteuerberechnung , 01 =
    rk - Römisch-Katholische Kirchensteuer, 02 = ev - Evangelische Kirchensteuer, 03 = lt - Evangelisch
    lutherisch (bis 12/2015), 04 = rf - Evangelisch reformiert (bis 12/2015), 05 = ak - Altkatholische
    Kirchensteuer, 06 = is - Israelitische / Jüdische Kultussteuer, 07 = fb - Freireligiöse
    Landesgemeinde Baden, 08 = ib - Israelitische Religionsgemeinschaft Baden, 09 = fo - Freireligiöse
    Gemeinde Offenbach/Main, 10 = fp - Freireligiöse Landesgemeinde Pfalz, 11 = fm - Freireligiöse
    Gemeinde Mainz, 12 = jü - Jüdisch, 13 = iw - Israelitische Religionsgemeinschaft Württembergs, 14 =
    if - Israelitische Kultussteuer Frankfurt, 15 = il - Israelitische Kultussteuer der
    kultusberechtigten Gemeinden, 16 = un - Unitarische Religionsgem. Freie Protestanten, 17 = fr -
    Französisch reformiert (bis 12/2015), 18 = fa - Freie Religionsgemeinschaft Alzey, 20 = fg -
    Freireligiöse Landesgemeinde Pfalz, 24 = jh - Jüdische Kultussteuer, 23 = jd - Jüdische
    Kultussteuer, 22 = ih - Jüdische Kultussteuer, 21 = fs - Freireligiöse Gemeinde Offenbach/Main
     |
    | **country**   |  0 = keine Angabe, A = Österreich, AFG = Afghanistan, AGO = Angola, AJ =
    Amerikanische Jungferninseln, AL = Albanien, AND = Andorra, ANG = Anguilla, ANT = Antigua und
    Barbuda, AQ = Antarktische Territorien, AQU = Äquatorialguinea, ARM = Armenien, AS = Amerikanisch
    Samoa, ASE = Aserbaidschan, AU = Korallenmeer-, Ashmore- und Cartierinseln, AUS = Australien, AW =
    Aruba, AX = Åland, B = Belgien, BD = Bangladesch, BDS = Barbados, BER = Bermuda, BG = Bulgarien, BH
    = Belize, BHT = Bhutan, BIH = Bosnien und Herzegowina, BIO = Malediven, BJ = Britische
    Jungferninseln, BL = St.Barthélemy, BOL = Bolivien, BQ = Bonaire, Saba, St.Eustatius, BR =
    Brasilien, BRN = Bahrain, BRU = Brunei Darussalam, BS = Bahamas, BV = Bouvetinsel, BY =
    Weissrussland, C = Kuba, CAM = Kamerun, CC = Kokosinseln, CDN = Kanada, CH = Schweiz, CHD = Tschad,
    CI = Côte d‘Ivoire, CL = Sri Lanka, CO = Kolumbien, COI = Cookinseln, CP = Clipperton, CR = Costa
    Rica, CV = Cabo Verde, CW = Curaçao, CY = Zypern, CX = Weihnachtsinsel, CZ = Tschechien, DK =
    Dänemark, DOM = Dominikanische Republik, DSC = Dschibuti, DY = Benin, DZ = Algerien, E = Spanien,
    EAK = Kenia, EAT = Tansania, EAU = Uganda, EC = Ecuador, EH = Westsahara, ERI = Eritrea, ES = El
    Salvador, EST = Estland, ET = Ägypten, ETH = Äthiopien, F = Frankreich, FAL = Falklandinseln, FG =
    Französisch Guayana, FIN = Finnland, FJI = Fidschi, FL = Liechtenstein, FP = Franz.-Polynesien, FR =
    Färöer, GAB = Gabun, GB = Vereinigtes Königreich, GCA = Guatemala, GEO = Georgien, GG = Guernsey, GH
    = Ghana, GIB = Gibraltar, GR = Griechenland, GRO = Grönland, GS = Südgeorgien und die südlichen
    Sandwichinseln, GUA = Guadeloupe, GUB = Guinea-Bissau, GUM = Guam, GUY = Guyana, H = Ungarn, HCA =
    Honduras, HEL = St. Helena /Ascension / Tristan da Cunha, HKG = Hongkong, HR = Kroatien, HM = Heard
    und McDonaldinseln, HV = Burkina Faso, I = Italien, IL = Israel, IND = Indien, IR = Iran, IRL =
    Irland, IRQ = Irak, IS = Island, IO = Britisches Territorium im Indischen Ozean, J = Japan, JA =
    Jamaika, JE = Jersey, JOR = Jordanien, K = Kambodscha, KAI = Kaimaninseln, KAN = Kanalinseln, KAS =
    Kasachstan, KIB = Kiribati, KIS = Kirgisistan, KOM = Komoren, KOR = Korea, Demokratische
    Volksrepublik (Nordkorea), KOS = Kosovo, KWT = Kuwait, L = Luxemburg, LAO = Laos, LAR = Libyen, LB =
    Liberia, LS = Lesotho, LT = Litauen, LV = Lettland, M = Malta, MA = Marokko, MAC = Macau, MAL =
    Malaysia, MAN = Insel Man, MAO = Oman, MAR = Marshallinseln, MAT = Martinique, MAY = Mayotte, MC =
    Monaco, MD = Moldau, MEX = Mexiko, MF = St.Martin (französischer Teil), MIK = Mikronesien, MK =
    Nordmazedonien, MNE = Montenegro, MON = Mongolei, MOT = Montserrat, MOZ = Mosambik, MS = Mauritius,
    MW = Malawi, MYA = Myanmar, N = Norwegen, NAU = Nauru, NEP = Nepal, NF = Norfolkinseln, NIC =
    Nicaragua, NIU = Niue, NKA = Neukaledonien, NL = Niederlande, NLA = Niederländische Antillen, NMA =
    Nördliche Marianen, NZ = Neuseeland, P = Portugal, PA = Panama, PAL = Palau, PE = Peru, PIE =
    St.Pierre und Miquelon, PIT = Pitcairninseln, PK = Pakistan, PL = Polen, PNG = Papua-Neuguinea, PRI
    = Puerto Rico, PSE = Palästinensische Gebiete, PY = Paraguay, QAT = Katar, RA = Argentinien, RB =
    Botsuana, RCA = Zentralafrikanische Republik, RCB = Kongo, RCH = Chile, REU = Réunion, RG = Guinea,
    RH = Haiti, RI = Indonesien, RIM = Mauretanien, RL = Libanon, RM = Madagaskar, RMM = Mali, RN =
    Niger, RO = Rumänien, ROK = Korea, Republik (Südkorea), ROU = Uruguay, RP = Philippinen, RSM = San
    Marino, RU = Burundi, RUS = Russische Föderation, RWA = Ruanda, S = Schweden, SAU = Saudi-Arabien,
    SCG = Serbien und Montenegro, SCN = St.Kitts und Nevis, SDN = Sudan, SGP = Singapur, SJ = Svalbard
    und Jan Mayen, SK = Slowakei, SLO = Slowenien, SME = Suriname, SN = Senegal, SOL = Salomonen, SP =
    Somalia, SRB = Serbien, SSD = Südsudan, STP = São Tomé und Príncipe, SWA =, SWZ = Namibia Eswatini,
    SY = Seychellen, SYR = Syrien, SX = St.Martin (niederländischer Teil), T = Thailand, TAD =
    Tadschikistan, TF = Französische Süd- und Antarktisgebiete, TG = Togo, TJ = China, TN = Tunesien,
    TOK = Tokelau, TON = Tonga, TR = Türkei, TT = Trinidad und Tobago, TUC = Turks- und Caicosinseln,
    TUR = Turkmenistan, TUV = Tuvalu, TWN = Taiwan, UA = Ukraine, UAE = Vereinigte Arabische Emirate, UM
    = Navassa / kleinere amerikanische Überseeinseln, USA = Vereinigte Staaten, USB = Usbekistan, V =
    Vatikanstadt, VAN = Vanuatu, VN = Vietnam, WAG = Gambia, WAL = Sierra Leone, WAN = Nigeria, WD =
    Dominica, WF = Wallis und Futuna, WG = Grenada, WL = St.Lucia, WS = Samoa, WV = St.Vincent und die
    Grenadinen, YEM = Jemen, YU = Jugoslawien, YV = Venezuela, Z = Sambia, ZA = Südafrika, ZRE = Kongo,
    Demokratische Republik, ZW = Simbabwe     |
    |  |   |
    | **nationality**   |   000 = Deutschland, 121 = Albanien, 122 = Bosnien und Herzegowina, 123 =
    Andorra, 124 = Belgien, 125 = Bulgarien, 126 = Dänemark, 127 = Estland, 128 = Finnland, 129 =
    Frankreich, 130 = Kroatien, 131 = Slowenien, 132 = Serbien und Montenegro, 133 = Serbien (einschl.
    Kosovo), 134 = Griechenland, 135 = Irland, 136 = Island, 137 = Italien, 138 = Jugoslawien, 139 =
    Lettland, 140 = Montenegro, 141 = Liechtenstein, 142 = Litauen, 143 = Luxemburg, 144 =
    Nordmazedonien, 145 = Malta, 146 = Moldau, 147 = Monaco, 148 = Niederlande, 149 = Norwegen, 150 =
    Kosovo, 151 = Österreich, 152 = Polen, 153 = Portugal, 154 = Rumänien, 155 = Slowakei, 156 = San
    Marino, 157 = Schweden, 158 = Schweiz, 160 = Russische Föderation, 161 = Spanien, 163 = Türkei, 164
    = Tschechien, 165 = Ungarn, 166 = Ukraine, 167 = Vatikanstadt, 168 = Vereinigtes Königreich , 169 =
    Weissrussland, 170 = Serbien, 181 = Zypern, 195 = Gibraltar, 199 = Übriges Europa, 221 = Algerien,
    223 = Angola, 224 = Eritrea, 225 = Äthiopien, 226 = Lesotho, 227 = Botsuana, 229 = Benin, 230 =
    Dschibuti, 231 = Côte d‘Ivoire, 232 = Nigeria, 233 = Simbabwe, 236 = Gabun, 237 = Gambia, 238 =
    Ghana, 239 = Mauretanien, 242 = Cabo Verde, 243 = Kenia, 244 = Komoren, 245 = Kongo, 246 = Kongo,
    Demokratische Republik, 247 = Liberia, 248 = Libyen, 249 = Madagaskar, 251 = Mali, 252 = Marokko,
    253 = Mauritius, 254 = Mosambik, 255 = Niger, 256 = Malawi, 257 = Sambia, 258 = Burkina Faso, 259 =
    Guinea-Bissau, 261 = Guinea, 262 = Kamerun, 263 = Südafrika, 265 = Ruanda, 267 = Namibia, 268 = São
    Tomé und Príncipe, 269 = Senegal, 271 = Seychellen, 272 = Sierra Leone, 273 = Somalia, 274 =
    Äquatorialguinea, 276 = Sudan (vor der Teilung des Landes), 277 = Sudan, 278 = Südsudan, 281 =
    Eswatini, 282 = Tansania, 283 = Togo, 284 = Tschad, 285 = Tunesien, 286 = Uganda, 287 = Ägypten, 289
    = Zentralafrikanische Republik, 291 = Burundi, 295 = Britisch abhängige Gebiete in Afrika, 299 =
    Übriges Afrika, 320 = Antigua und Barbuda, 322 = Barbados, 323 = Argentinien, 324 = Bahamas, 326 =
    Bolivien, 327 = Brasilien, 328 = Guyana, 330 = Belize, 332 = Chile, 333 = Dominica, 334 = Costa
    Rica, 335 = Dominikanische Republik, 336 = Ecuador, 337 = El Salvador, 340 = Grenada, 345 =
    Guatemala, 346 = Haiti, 347 = Honduras, 348 = Kanada, 349 = Kolumbien, 351 = Kuba, 353 = Mexiko, 354
    = Nicaragua, 355 = Jamaika, 357 = Panama, 359 = Paraguay, 361 = Peru, 364 = Suriname, 365 = Uruguay,
    366 = St. Lucia, 367 = Venezuela, 368 = Vereinigte Staaten, 369 = St. Vincent und die Grenadinen,
    370 = St. Kitts und Nevis, 371 = Trinidad und Tobago, 395 = Britisch abhängige Gebiete in Amerika,
    399 = Übriges Amerika, 411 = Hongkong, 412 =  Macau, 421 = Jemen, 422 = Armenien, 423 = Afghanistan,
    424 = Bahrain, 425 = Aserbaidschan, 426 = Bhutan, 427 = Myanmar, 429 = Brunei Darussalam, 430 =
    Georgien, 431 = Sri Lanka, 432 = Vietnam, 434 = Korea, Demokratische Volksrepublik (Nordkorea), 436
    = Indien, 437 = Indonesien, 438 = Irak, 439 = Iran, 441 = Israel, 442 = Japan, 444 = Kasachstan, 445
    = Jordanien, 446 = Kambodscha, 447 = Katar, 448 = Kuwait, 449 = Laos, 450 = Kirgisistan, 451 =
    Libanon, 454 = Malediven, 456 = Oman, 457 = Mongolei, 458 = Nepal, 459 = Palästinensische Gebiete,
    460 = Bangladesch, 461 = Pakistan, 462 = Philippinen, 465 = Taiwan, 467 = Korea, Republik
    (Südkorea), 469 = Vereinigte Arabische Emirate, 470 = Tadschikistan, 471 = Turkmenistan, 472 =
    Saudi-Arabien, 474 = Singapur, 475 = Syrien, 476 = Thailand, 477 = Usbekistan, 479 = China, 482 =
    Malaysia, 499 = Übriges Asien, 523 = Australien, 524 = Salomonen, 525 = Nördliche Marianen, 526 =
    Fidschi, 530 = Kiribati, 531 = Nauru, 532 = Vanuatu, 536 = Neuseeland, 537 = Palau, 538 = Papua-
    Neuguinea, 540 = Tuvalu, 541 = Tonga, 543 = Samoa, 544 = Marshallinseln, 545 = Mikronesien, 595 =
    Britisch abh. Gebiete in Australien/Ozeanien, 599 = Übriges Ozeanien, 996 = Unbekanntes Ausland, 997
    = staatenlos, 998 = ungeklärt, 999 = ohne Angabe    |
    |  |   |
    | **contribution_class_health_insurance**   |    0 = kein Beitrag (private KV oder frw. KV als
    Selbstzahler), 1 = allgemeiner Beitrag, 3 = ermäßigter Beitrag, 4 = Beitrag zur landwirtschaftlichen
    KV, 5 = Arbeitgeberbeitrag zur landwirtschaftlichen KV, 6 = Pauschalbeitrag für geringfügig
    Beschäftigte, 9 = Firmenzahler    |
    | **contribution_class_pension_insurance**   |   0 = kein Beitrag, 1 = voller Beitrag, 3 = halber
    Beitrag, 5 = Pauschalbeitrag für geringfügig Beschäftigte     |
    | **contribution_class_unemployment_insurance**   |    0 = kein Beitrag zur BA, 1 = voller Beitrag
    zur BA, 2 = halber Beitrag zur BA    |
    | **contribution_class_long_term_care_insurance**   |   0 = kein Beitrag zur gesetzl. PV, 1 = voller
    Beitrag zur gesetzl. PV, 2 = halber Beitrag zur gesetzl. PV    |
    | **person_group_key**   |  Lodas:  0 = keine Angabe, 101 = Sozialversicherungspflichtig
    Beschäftigte ohne besondere Merkmale, 102 = Auszubildende ohne besondere Merkmale, 103 =
    Beschäftigte in Altersteilzeit, 104 = Hausgewerbetreibende ( nicht Heimarbeiter ), 105 =
    Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in anerkannten Werkstätten oder
    gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109 = Geringfügig entlohnte
    Beschäftigte nach §8Abs.1 Nr.1 SGB IV, 110 = Kurzfristig Beschäftigte nach §8Abs.1 Nr.2 SGB IV, 111
    = Personen in Berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige
    in der Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal
    beschäftigt, 116 = Ausgleichsgeldempfänger nach dem FELEG, 118 = Unständig Beschäftigte, 119 =
    Versicherungsfr. Altersvollrentner/Versorgungsbezieher wg. Alters, 120 = Versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 121 = Auszubildende, deren Arbeitsentgelt die
    Geringverdienergrenze nicht übersteigt, 122 = Auszubildende in einer außerbetrieblichen Einrichtung,
    123 = Personen, die ein freiwilliges soziales oder ökologisches Jahr oder BFD leisten, 124 =
    Heimarbeiter ohne Entgeltfortzahlungsanspruch, 127 = Behinderte Menschen, die in einem
    Integrationsprojekt beschäftigt sind, 140 = Seeleute, 141 = Auszubildende in der Seefahrt (mit
    Arbeitsentgelt), 142 = Seeleute in Altersteilzeit, 143 = Seelotsen, 144 = Auszubildende in der
    Seefahrt, Arbeitsentgelt bis zur Geringverdienergrenze, 149 = In Seefahrt besch. versicherungsfr.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 150 = In Seefahrt besch. versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 190 = Beschäftigte, die nur in der gesetzlichen
    Unfallversicherung versichert sind  |
    |                        |  Lohn und Gehalt:  101 = Sozialversicherungspflichtig Beschäftigte, 102 =
    Auszubildende ohne besondere Merkmale, 103 = Beschäftigte in Altersteilzeit, 104 =
    Hausgewerbetreibende, 105 = Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in
    anerkannten Werkstätten oder gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109
    = Geringfügig entlohnte Beschäftigte, 110 = Kurzfristig Beschäftigte, 111 = Personen in
    berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige in der
    Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal beschäftigt, 116
    = Ausgleichsgeldempfänger nach dem FELEG, 118 = Berufsmäßig unständig Beschäftigte, 119 =
    Versicherungsfreie Altersvollrentner und Versorgungsbezieher wegen Alters, 120 =
    Versicherungspflichtige Altersvollrentner, 140 = Seeleute, 141 = Auszubildende in der Seefahrt, 142
    = Seeleute in Altersteilzeit, 143 = Seelotsen, 900 = Nicht meldepflichtig Beschäftigte, 127 =
    Behinderte Menschen, die in einem Integrationsprojekt beschäftigt sind, 190 = Beschäftigte, die nur
    in der gesetzlichen Unfallversicherung versichert sind, 144 = Auszubildende in der Seefahrt,
    Arbeitsentgelt bis zur Geringverdienergrenze, 123 = Personen, die ein freiwilliges soziales oder
    ökologisches Jahr oder BFD leisten, 122 = Auszubildende in einer außerbetrieblichen Einrichtung, 121
    = Auszubildende, deren Arbeitsentgelt die Geringverdienergrenze nicht übersteigt, 149 =
    Versicherungsfreie Altersvollrentner in der Seefahrt und Versorgungsbezieher, 124 = Heimarbeiter
    ohne Entgeltfortzahlungsanspruch, 117 = Nicht berufsmäßig unständig Beschäftigte, |
    |  |   |
    | **occupational_classification_code** | Ausgeübte Tätigkeit siehe:
    https://www.arbeitsagentur.de/datei/dok_ba015567.pdf   |
    | **occupational_classification_code_employee_leasing** | 0 = Keine_Angabe, 1 = nein, 2 = ja  |
    | **type_of_contract** |  0 = Keine_Angabe, 1 = Unbefristet in Vollzeit, 2 = Unbefristet in
    Teilzeit, 3 = Befristet in Vollzeit, 4 = Befristet in Teilzeit |
    |  |   |
    | **highest_level_of_professional_training** | 0 = Keine_Angabe, 1 = Ohne Ausbildungsabschluss, 2 =
    Ausbildungsabschluss, 3 = Meister, 4 = Bachelor, 5 = Diplom, 6 = Promotion, 9 = Abschluss unbekannt
    |
    | **highest_level_of_education** | 0 = Keine_Angabe, 1 = Ohne Schulabschluss, 2 =
    Hauptschulabschluss, 3 = Mittlere Reife, 4 = Abitur, 9 = Abschluss unbekannt  |
    | **is_ignore_additional_contribution_to_long_term_care_insurance_for_childless** | 0 = Nein, 1 = Ja
    |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    """ Get the list of employees' masterdata

     Masterdata of all employees can be accessed by the client's client-id.



     If a non-mandatory field is not filled in the payroll system, the field will not be exported
    through the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **sex**   |  Lodas: 0 = männlich, 1 = weiblich, 2 = divers, 3 = unbestimmt  |
    |           |  Lohn und Gehalt: 0 = weiblich, 1 = männlich, 2 = divers, 3 = unbestimmt |
    | **denomination/spouses_denomination**  |  Lodas:  0 = Konfessionslos / Keine
    Kirchensteuerberechnung, 1 = ev - Evangelische Kirchensteuer, 2 = rk - Römisch-Katholische
    Kirchensteuer, 3 = ak - Altkatholische Kirchensteuer, 4 = fa - Freie Religionsgemeinschaft Alzey, 5
    = fb - Freireligiöse Landesgemeinde Baden, 6 = fg - Freireligiöse Landesgemeinde Pfalz, 7 = fm -
    Freireligiöse Gemeinde Mainz, 8 = fr - Französisch reformiert (bis 12/2015), 9 = fs - Freireligiöse
    Gemeinde Offenbach/Main, 10 = ib - Israelitische Religionsgemeinschaft Baden, 11 = ih - Jüdische
    Kultussteuer, 12 = il - Israelitische Kultussteuer der kultusberechtigten Gemeinden, 13 = is -
    Israelitische / Jüdische Kultussteuer, 14 = iw - Israelitische Religionsgemeinschaft Württembergs,
    15 = jd - Jüdische Kultussteuer, 16 = jh - Jüdische Kultussteuer, 17 = lt - Evangelisch lutherisch
    (bis 12/2015), 18 = rf - Evangelisch reformiert (bis 12/2015) |
    |                    |  Lohn und Gehalt:  00 = Konfessionslos / Keine Kirchensteuerberechnung , 01 =
    rk - Römisch-Katholische Kirchensteuer, 02 = ev - Evangelische Kirchensteuer, 03 = lt - Evangelisch
    lutherisch (bis 12/2015), 04 = rf - Evangelisch reformiert (bis 12/2015), 05 = ak - Altkatholische
    Kirchensteuer, 06 = is - Israelitische / Jüdische Kultussteuer, 07 = fb - Freireligiöse
    Landesgemeinde Baden, 08 = ib - Israelitische Religionsgemeinschaft Baden, 09 = fo - Freireligiöse
    Gemeinde Offenbach/Main, 10 = fp - Freireligiöse Landesgemeinde Pfalz, 11 = fm - Freireligiöse
    Gemeinde Mainz, 12 = jü - Jüdisch, 13 = iw - Israelitische Religionsgemeinschaft Württembergs, 14 =
    if - Israelitische Kultussteuer Frankfurt, 15 = il - Israelitische Kultussteuer der
    kultusberechtigten Gemeinden, 16 = un - Unitarische Religionsgem. Freie Protestanten, 17 = fr -
    Französisch reformiert (bis 12/2015), 18 = fa - Freie Religionsgemeinschaft Alzey, 20 = fg -
    Freireligiöse Landesgemeinde Pfalz, 24 = jh - Jüdische Kultussteuer, 23 = jd - Jüdische
    Kultussteuer, 22 = ih - Jüdische Kultussteuer, 21 = fs - Freireligiöse Gemeinde Offenbach/Main
     |
    | **country**   |  0 = keine Angabe, A = Österreich, AFG = Afghanistan, AGO = Angola, AJ =
    Amerikanische Jungferninseln, AL = Albanien, AND = Andorra, ANG = Anguilla, ANT = Antigua und
    Barbuda, AQ = Antarktische Territorien, AQU = Äquatorialguinea, ARM = Armenien, AS = Amerikanisch
    Samoa, ASE = Aserbaidschan, AU = Korallenmeer-, Ashmore- und Cartierinseln, AUS = Australien, AW =
    Aruba, AX = Åland, B = Belgien, BD = Bangladesch, BDS = Barbados, BER = Bermuda, BG = Bulgarien, BH
    = Belize, BHT = Bhutan, BIH = Bosnien und Herzegowina, BIO = Malediven, BJ = Britische
    Jungferninseln, BL = St.Barthélemy, BOL = Bolivien, BQ = Bonaire, Saba, St.Eustatius, BR =
    Brasilien, BRN = Bahrain, BRU = Brunei Darussalam, BS = Bahamas, BV = Bouvetinsel, BY =
    Weissrussland, C = Kuba, CAM = Kamerun, CC = Kokosinseln, CDN = Kanada, CH = Schweiz, CHD = Tschad,
    CI = Côte d‘Ivoire, CL = Sri Lanka, CO = Kolumbien, COI = Cookinseln, CP = Clipperton, CR = Costa
    Rica, CV = Cabo Verde, CW = Curaçao, CY = Zypern, CX = Weihnachtsinsel, CZ = Tschechien, DK =
    Dänemark, DOM = Dominikanische Republik, DSC = Dschibuti, DY = Benin, DZ = Algerien, E = Spanien,
    EAK = Kenia, EAT = Tansania, EAU = Uganda, EC = Ecuador, EH = Westsahara, ERI = Eritrea, ES = El
    Salvador, EST = Estland, ET = Ägypten, ETH = Äthiopien, F = Frankreich, FAL = Falklandinseln, FG =
    Französisch Guayana, FIN = Finnland, FJI = Fidschi, FL = Liechtenstein, FP = Franz.-Polynesien, FR =
    Färöer, GAB = Gabun, GB = Vereinigtes Königreich, GCA = Guatemala, GEO = Georgien, GG = Guernsey, GH
    = Ghana, GIB = Gibraltar, GR = Griechenland, GRO = Grönland, GS = Südgeorgien und die südlichen
    Sandwichinseln, GUA = Guadeloupe, GUB = Guinea-Bissau, GUM = Guam, GUY = Guyana, H = Ungarn, HCA =
    Honduras, HEL = St. Helena /Ascension / Tristan da Cunha, HKG = Hongkong, HR = Kroatien, HM = Heard
    und McDonaldinseln, HV = Burkina Faso, I = Italien, IL = Israel, IND = Indien, IR = Iran, IRL =
    Irland, IRQ = Irak, IS = Island, IO = Britisches Territorium im Indischen Ozean, J = Japan, JA =
    Jamaika, JE = Jersey, JOR = Jordanien, K = Kambodscha, KAI = Kaimaninseln, KAN = Kanalinseln, KAS =
    Kasachstan, KIB = Kiribati, KIS = Kirgisistan, KOM = Komoren, KOR = Korea, Demokratische
    Volksrepublik (Nordkorea), KOS = Kosovo, KWT = Kuwait, L = Luxemburg, LAO = Laos, LAR = Libyen, LB =
    Liberia, LS = Lesotho, LT = Litauen, LV = Lettland, M = Malta, MA = Marokko, MAC = Macau, MAL =
    Malaysia, MAN = Insel Man, MAO = Oman, MAR = Marshallinseln, MAT = Martinique, MAY = Mayotte, MC =
    Monaco, MD = Moldau, MEX = Mexiko, MF = St.Martin (französischer Teil), MIK = Mikronesien, MK =
    Nordmazedonien, MNE = Montenegro, MON = Mongolei, MOT = Montserrat, MOZ = Mosambik, MS = Mauritius,
    MW = Malawi, MYA = Myanmar, N = Norwegen, NAU = Nauru, NEP = Nepal, NF = Norfolkinseln, NIC =
    Nicaragua, NIU = Niue, NKA = Neukaledonien, NL = Niederlande, NLA = Niederländische Antillen, NMA =
    Nördliche Marianen, NZ = Neuseeland, P = Portugal, PA = Panama, PAL = Palau, PE = Peru, PIE =
    St.Pierre und Miquelon, PIT = Pitcairninseln, PK = Pakistan, PL = Polen, PNG = Papua-Neuguinea, PRI
    = Puerto Rico, PSE = Palästinensische Gebiete, PY = Paraguay, QAT = Katar, RA = Argentinien, RB =
    Botsuana, RCA = Zentralafrikanische Republik, RCB = Kongo, RCH = Chile, REU = Réunion, RG = Guinea,
    RH = Haiti, RI = Indonesien, RIM = Mauretanien, RL = Libanon, RM = Madagaskar, RMM = Mali, RN =
    Niger, RO = Rumänien, ROK = Korea, Republik (Südkorea), ROU = Uruguay, RP = Philippinen, RSM = San
    Marino, RU = Burundi, RUS = Russische Föderation, RWA = Ruanda, S = Schweden, SAU = Saudi-Arabien,
    SCG = Serbien und Montenegro, SCN = St.Kitts und Nevis, SDN = Sudan, SGP = Singapur, SJ = Svalbard
    und Jan Mayen, SK = Slowakei, SLO = Slowenien, SME = Suriname, SN = Senegal, SOL = Salomonen, SP =
    Somalia, SRB = Serbien, SSD = Südsudan, STP = São Tomé und Príncipe, SWA =, SWZ = Namibia Eswatini,
    SY = Seychellen, SYR = Syrien, SX = St.Martin (niederländischer Teil), T = Thailand, TAD =
    Tadschikistan, TF = Französische Süd- und Antarktisgebiete, TG = Togo, TJ = China, TN = Tunesien,
    TOK = Tokelau, TON = Tonga, TR = Türkei, TT = Trinidad und Tobago, TUC = Turks- und Caicosinseln,
    TUR = Turkmenistan, TUV = Tuvalu, TWN = Taiwan, UA = Ukraine, UAE = Vereinigte Arabische Emirate, UM
    = Navassa / kleinere amerikanische Überseeinseln, USA = Vereinigte Staaten, USB = Usbekistan, V =
    Vatikanstadt, VAN = Vanuatu, VN = Vietnam, WAG = Gambia, WAL = Sierra Leone, WAN = Nigeria, WD =
    Dominica, WF = Wallis und Futuna, WG = Grenada, WL = St.Lucia, WS = Samoa, WV = St.Vincent und die
    Grenadinen, YEM = Jemen, YU = Jugoslawien, YV = Venezuela, Z = Sambia, ZA = Südafrika, ZRE = Kongo,
    Demokratische Republik, ZW = Simbabwe     |
    |  |   |
    | **nationality**   |   000 = Deutschland, 121 = Albanien, 122 = Bosnien und Herzegowina, 123 =
    Andorra, 124 = Belgien, 125 = Bulgarien, 126 = Dänemark, 127 = Estland, 128 = Finnland, 129 =
    Frankreich, 130 = Kroatien, 131 = Slowenien, 132 = Serbien und Montenegro, 133 = Serbien (einschl.
    Kosovo), 134 = Griechenland, 135 = Irland, 136 = Island, 137 = Italien, 138 = Jugoslawien, 139 =
    Lettland, 140 = Montenegro, 141 = Liechtenstein, 142 = Litauen, 143 = Luxemburg, 144 =
    Nordmazedonien, 145 = Malta, 146 = Moldau, 147 = Monaco, 148 = Niederlande, 149 = Norwegen, 150 =
    Kosovo, 151 = Österreich, 152 = Polen, 153 = Portugal, 154 = Rumänien, 155 = Slowakei, 156 = San
    Marino, 157 = Schweden, 158 = Schweiz, 160 = Russische Föderation, 161 = Spanien, 163 = Türkei, 164
    = Tschechien, 165 = Ungarn, 166 = Ukraine, 167 = Vatikanstadt, 168 = Vereinigtes Königreich , 169 =
    Weissrussland, 170 = Serbien, 181 = Zypern, 195 = Gibraltar, 199 = Übriges Europa, 221 = Algerien,
    223 = Angola, 224 = Eritrea, 225 = Äthiopien, 226 = Lesotho, 227 = Botsuana, 229 = Benin, 230 =
    Dschibuti, 231 = Côte d‘Ivoire, 232 = Nigeria, 233 = Simbabwe, 236 = Gabun, 237 = Gambia, 238 =
    Ghana, 239 = Mauretanien, 242 = Cabo Verde, 243 = Kenia, 244 = Komoren, 245 = Kongo, 246 = Kongo,
    Demokratische Republik, 247 = Liberia, 248 = Libyen, 249 = Madagaskar, 251 = Mali, 252 = Marokko,
    253 = Mauritius, 254 = Mosambik, 255 = Niger, 256 = Malawi, 257 = Sambia, 258 = Burkina Faso, 259 =
    Guinea-Bissau, 261 = Guinea, 262 = Kamerun, 263 = Südafrika, 265 = Ruanda, 267 = Namibia, 268 = São
    Tomé und Príncipe, 269 = Senegal, 271 = Seychellen, 272 = Sierra Leone, 273 = Somalia, 274 =
    Äquatorialguinea, 276 = Sudan (vor der Teilung des Landes), 277 = Sudan, 278 = Südsudan, 281 =
    Eswatini, 282 = Tansania, 283 = Togo, 284 = Tschad, 285 = Tunesien, 286 = Uganda, 287 = Ägypten, 289
    = Zentralafrikanische Republik, 291 = Burundi, 295 = Britisch abhängige Gebiete in Afrika, 299 =
    Übriges Afrika, 320 = Antigua und Barbuda, 322 = Barbados, 323 = Argentinien, 324 = Bahamas, 326 =
    Bolivien, 327 = Brasilien, 328 = Guyana, 330 = Belize, 332 = Chile, 333 = Dominica, 334 = Costa
    Rica, 335 = Dominikanische Republik, 336 = Ecuador, 337 = El Salvador, 340 = Grenada, 345 =
    Guatemala, 346 = Haiti, 347 = Honduras, 348 = Kanada, 349 = Kolumbien, 351 = Kuba, 353 = Mexiko, 354
    = Nicaragua, 355 = Jamaika, 357 = Panama, 359 = Paraguay, 361 = Peru, 364 = Suriname, 365 = Uruguay,
    366 = St. Lucia, 367 = Venezuela, 368 = Vereinigte Staaten, 369 = St. Vincent und die Grenadinen,
    370 = St. Kitts und Nevis, 371 = Trinidad und Tobago, 395 = Britisch abhängige Gebiete in Amerika,
    399 = Übriges Amerika, 411 = Hongkong, 412 =  Macau, 421 = Jemen, 422 = Armenien, 423 = Afghanistan,
    424 = Bahrain, 425 = Aserbaidschan, 426 = Bhutan, 427 = Myanmar, 429 = Brunei Darussalam, 430 =
    Georgien, 431 = Sri Lanka, 432 = Vietnam, 434 = Korea, Demokratische Volksrepublik (Nordkorea), 436
    = Indien, 437 = Indonesien, 438 = Irak, 439 = Iran, 441 = Israel, 442 = Japan, 444 = Kasachstan, 445
    = Jordanien, 446 = Kambodscha, 447 = Katar, 448 = Kuwait, 449 = Laos, 450 = Kirgisistan, 451 =
    Libanon, 454 = Malediven, 456 = Oman, 457 = Mongolei, 458 = Nepal, 459 = Palästinensische Gebiete,
    460 = Bangladesch, 461 = Pakistan, 462 = Philippinen, 465 = Taiwan, 467 = Korea, Republik
    (Südkorea), 469 = Vereinigte Arabische Emirate, 470 = Tadschikistan, 471 = Turkmenistan, 472 =
    Saudi-Arabien, 474 = Singapur, 475 = Syrien, 476 = Thailand, 477 = Usbekistan, 479 = China, 482 =
    Malaysia, 499 = Übriges Asien, 523 = Australien, 524 = Salomonen, 525 = Nördliche Marianen, 526 =
    Fidschi, 530 = Kiribati, 531 = Nauru, 532 = Vanuatu, 536 = Neuseeland, 537 = Palau, 538 = Papua-
    Neuguinea, 540 = Tuvalu, 541 = Tonga, 543 = Samoa, 544 = Marshallinseln, 545 = Mikronesien, 595 =
    Britisch abh. Gebiete in Australien/Ozeanien, 599 = Übriges Ozeanien, 996 = Unbekanntes Ausland, 997
    = staatenlos, 998 = ungeklärt, 999 = ohne Angabe    |
    |  |   |
    | **contribution_class_health_insurance**   |    0 = kein Beitrag (private KV oder frw. KV als
    Selbstzahler), 1 = allgemeiner Beitrag, 3 = ermäßigter Beitrag, 4 = Beitrag zur landwirtschaftlichen
    KV, 5 = Arbeitgeberbeitrag zur landwirtschaftlichen KV, 6 = Pauschalbeitrag für geringfügig
    Beschäftigte, 9 = Firmenzahler    |
    | **contribution_class_pension_insurance**   |   0 = kein Beitrag, 1 = voller Beitrag, 3 = halber
    Beitrag, 5 = Pauschalbeitrag für geringfügig Beschäftigte     |
    | **contribution_class_unemployment_insurance**   |    0 = kein Beitrag zur BA, 1 = voller Beitrag
    zur BA, 2 = halber Beitrag zur BA    |
    | **contribution_class_long_term_care_insurance**   |   0 = kein Beitrag zur gesetzl. PV, 1 = voller
    Beitrag zur gesetzl. PV, 2 = halber Beitrag zur gesetzl. PV    |
    | **person_group_key**   |  Lodas:  0 = keine Angabe, 101 = Sozialversicherungspflichtig
    Beschäftigte ohne besondere Merkmale, 102 = Auszubildende ohne besondere Merkmale, 103 =
    Beschäftigte in Altersteilzeit, 104 = Hausgewerbetreibende ( nicht Heimarbeiter ), 105 =
    Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in anerkannten Werkstätten oder
    gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109 = Geringfügig entlohnte
    Beschäftigte nach §8Abs.1 Nr.1 SGB IV, 110 = Kurzfristig Beschäftigte nach §8Abs.1 Nr.2 SGB IV, 111
    = Personen in Berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige
    in der Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal
    beschäftigt, 116 = Ausgleichsgeldempfänger nach dem FELEG, 118 = Unständig Beschäftigte, 119 =
    Versicherungsfr. Altersvollrentner/Versorgungsbezieher wg. Alters, 120 = Versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 121 = Auszubildende, deren Arbeitsentgelt die
    Geringverdienergrenze nicht übersteigt, 122 = Auszubildende in einer außerbetrieblichen Einrichtung,
    123 = Personen, die ein freiwilliges soziales oder ökologisches Jahr oder BFD leisten, 124 =
    Heimarbeiter ohne Entgeltfortzahlungsanspruch, 127 = Behinderte Menschen, die in einem
    Integrationsprojekt beschäftigt sind, 140 = Seeleute, 141 = Auszubildende in der Seefahrt (mit
    Arbeitsentgelt), 142 = Seeleute in Altersteilzeit, 143 = Seelotsen, 144 = Auszubildende in der
    Seefahrt, Arbeitsentgelt bis zur Geringverdienergrenze, 149 = In Seefahrt besch. versicherungsfr.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 150 = In Seefahrt besch. versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 190 = Beschäftigte, die nur in der gesetzlichen
    Unfallversicherung versichert sind  |
    |                        |  Lohn und Gehalt:  101 = Sozialversicherungspflichtig Beschäftigte, 102 =
    Auszubildende ohne besondere Merkmale, 103 = Beschäftigte in Altersteilzeit, 104 =
    Hausgewerbetreibende, 105 = Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in
    anerkannten Werkstätten oder gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109
    = Geringfügig entlohnte Beschäftigte, 110 = Kurzfristig Beschäftigte, 111 = Personen in
    berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige in der
    Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal beschäftigt, 116
    = Ausgleichsgeldempfänger nach dem FELEG, 118 = Berufsmäßig unständig Beschäftigte, 119 =
    Versicherungsfreie Altersvollrentner und Versorgungsbezieher wegen Alters, 120 =
    Versicherungspflichtige Altersvollrentner, 140 = Seeleute, 141 = Auszubildende in der Seefahrt, 142
    = Seeleute in Altersteilzeit, 143 = Seelotsen, 900 = Nicht meldepflichtig Beschäftigte, 127 =
    Behinderte Menschen, die in einem Integrationsprojekt beschäftigt sind, 190 = Beschäftigte, die nur
    in der gesetzlichen Unfallversicherung versichert sind, 144 = Auszubildende in der Seefahrt,
    Arbeitsentgelt bis zur Geringverdienergrenze, 123 = Personen, die ein freiwilliges soziales oder
    ökologisches Jahr oder BFD leisten, 122 = Auszubildende in einer außerbetrieblichen Einrichtung, 121
    = Auszubildende, deren Arbeitsentgelt die Geringverdienergrenze nicht übersteigt, 149 =
    Versicherungsfreie Altersvollrentner in der Seefahrt und Versorgungsbezieher, 124 = Heimarbeiter
    ohne Entgeltfortzahlungsanspruch, 117 = Nicht berufsmäßig unständig Beschäftigte, |
    |  |   |
    | **occupational_classification_code** | Ausgeübte Tätigkeit siehe:
    https://www.arbeitsagentur.de/datei/dok_ba015567.pdf   |
    | **occupational_classification_code_employee_leasing** | 0 = Keine_Angabe, 1 = nein, 2 = ja  |
    | **type_of_contract** |  0 = Keine_Angabe, 1 = Unbefristet in Vollzeit, 2 = Unbefristet in
    Teilzeit, 3 = Befristet in Vollzeit, 4 = Befristet in Teilzeit |
    |  |   |
    | **highest_level_of_professional_training** | 0 = Keine_Angabe, 1 = Ohne Ausbildungsabschluss, 2 =
    Ausbildungsabschluss, 3 = Meister, 4 = Bachelor, 5 = Diplom, 6 = Promotion, 9 = Abschluss unbekannt
    |
    | **highest_level_of_education** | 0 = Keine_Angabe, 1 = Ohne Schulabschluss, 2 =
    Hauptschulabschluss, 3 = Mittlere Reife, 4 = Abitur, 9 = Abschluss unbekannt  |
    | **is_ignore_additional_contribution_to_long_term_care_insurance_for_childless** | 0 = Nein, 1 = Ja
    |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    """ Get the list of employees' masterdata

     Masterdata of all employees can be accessed by the client's client-id.



     If a non-mandatory field is not filled in the payroll system, the field will not be exported
    through the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **sex**   |  Lodas: 0 = männlich, 1 = weiblich, 2 = divers, 3 = unbestimmt  |
    |           |  Lohn und Gehalt: 0 = weiblich, 1 = männlich, 2 = divers, 3 = unbestimmt |
    | **denomination/spouses_denomination**  |  Lodas:  0 = Konfessionslos / Keine
    Kirchensteuerberechnung, 1 = ev - Evangelische Kirchensteuer, 2 = rk - Römisch-Katholische
    Kirchensteuer, 3 = ak - Altkatholische Kirchensteuer, 4 = fa - Freie Religionsgemeinschaft Alzey, 5
    = fb - Freireligiöse Landesgemeinde Baden, 6 = fg - Freireligiöse Landesgemeinde Pfalz, 7 = fm -
    Freireligiöse Gemeinde Mainz, 8 = fr - Französisch reformiert (bis 12/2015), 9 = fs - Freireligiöse
    Gemeinde Offenbach/Main, 10 = ib - Israelitische Religionsgemeinschaft Baden, 11 = ih - Jüdische
    Kultussteuer, 12 = il - Israelitische Kultussteuer der kultusberechtigten Gemeinden, 13 = is -
    Israelitische / Jüdische Kultussteuer, 14 = iw - Israelitische Religionsgemeinschaft Württembergs,
    15 = jd - Jüdische Kultussteuer, 16 = jh - Jüdische Kultussteuer, 17 = lt - Evangelisch lutherisch
    (bis 12/2015), 18 = rf - Evangelisch reformiert (bis 12/2015) |
    |                    |  Lohn und Gehalt:  00 = Konfessionslos / Keine Kirchensteuerberechnung , 01 =
    rk - Römisch-Katholische Kirchensteuer, 02 = ev - Evangelische Kirchensteuer, 03 = lt - Evangelisch
    lutherisch (bis 12/2015), 04 = rf - Evangelisch reformiert (bis 12/2015), 05 = ak - Altkatholische
    Kirchensteuer, 06 = is - Israelitische / Jüdische Kultussteuer, 07 = fb - Freireligiöse
    Landesgemeinde Baden, 08 = ib - Israelitische Religionsgemeinschaft Baden, 09 = fo - Freireligiöse
    Gemeinde Offenbach/Main, 10 = fp - Freireligiöse Landesgemeinde Pfalz, 11 = fm - Freireligiöse
    Gemeinde Mainz, 12 = jü - Jüdisch, 13 = iw - Israelitische Religionsgemeinschaft Württembergs, 14 =
    if - Israelitische Kultussteuer Frankfurt, 15 = il - Israelitische Kultussteuer der
    kultusberechtigten Gemeinden, 16 = un - Unitarische Religionsgem. Freie Protestanten, 17 = fr -
    Französisch reformiert (bis 12/2015), 18 = fa - Freie Religionsgemeinschaft Alzey, 20 = fg -
    Freireligiöse Landesgemeinde Pfalz, 24 = jh - Jüdische Kultussteuer, 23 = jd - Jüdische
    Kultussteuer, 22 = ih - Jüdische Kultussteuer, 21 = fs - Freireligiöse Gemeinde Offenbach/Main
     |
    | **country**   |  0 = keine Angabe, A = Österreich, AFG = Afghanistan, AGO = Angola, AJ =
    Amerikanische Jungferninseln, AL = Albanien, AND = Andorra, ANG = Anguilla, ANT = Antigua und
    Barbuda, AQ = Antarktische Territorien, AQU = Äquatorialguinea, ARM = Armenien, AS = Amerikanisch
    Samoa, ASE = Aserbaidschan, AU = Korallenmeer-, Ashmore- und Cartierinseln, AUS = Australien, AW =
    Aruba, AX = Åland, B = Belgien, BD = Bangladesch, BDS = Barbados, BER = Bermuda, BG = Bulgarien, BH
    = Belize, BHT = Bhutan, BIH = Bosnien und Herzegowina, BIO = Malediven, BJ = Britische
    Jungferninseln, BL = St.Barthélemy, BOL = Bolivien, BQ = Bonaire, Saba, St.Eustatius, BR =
    Brasilien, BRN = Bahrain, BRU = Brunei Darussalam, BS = Bahamas, BV = Bouvetinsel, BY =
    Weissrussland, C = Kuba, CAM = Kamerun, CC = Kokosinseln, CDN = Kanada, CH = Schweiz, CHD = Tschad,
    CI = Côte d‘Ivoire, CL = Sri Lanka, CO = Kolumbien, COI = Cookinseln, CP = Clipperton, CR = Costa
    Rica, CV = Cabo Verde, CW = Curaçao, CY = Zypern, CX = Weihnachtsinsel, CZ = Tschechien, DK =
    Dänemark, DOM = Dominikanische Republik, DSC = Dschibuti, DY = Benin, DZ = Algerien, E = Spanien,
    EAK = Kenia, EAT = Tansania, EAU = Uganda, EC = Ecuador, EH = Westsahara, ERI = Eritrea, ES = El
    Salvador, EST = Estland, ET = Ägypten, ETH = Äthiopien, F = Frankreich, FAL = Falklandinseln, FG =
    Französisch Guayana, FIN = Finnland, FJI = Fidschi, FL = Liechtenstein, FP = Franz.-Polynesien, FR =
    Färöer, GAB = Gabun, GB = Vereinigtes Königreich, GCA = Guatemala, GEO = Georgien, GG = Guernsey, GH
    = Ghana, GIB = Gibraltar, GR = Griechenland, GRO = Grönland, GS = Südgeorgien und die südlichen
    Sandwichinseln, GUA = Guadeloupe, GUB = Guinea-Bissau, GUM = Guam, GUY = Guyana, H = Ungarn, HCA =
    Honduras, HEL = St. Helena /Ascension / Tristan da Cunha, HKG = Hongkong, HR = Kroatien, HM = Heard
    und McDonaldinseln, HV = Burkina Faso, I = Italien, IL = Israel, IND = Indien, IR = Iran, IRL =
    Irland, IRQ = Irak, IS = Island, IO = Britisches Territorium im Indischen Ozean, J = Japan, JA =
    Jamaika, JE = Jersey, JOR = Jordanien, K = Kambodscha, KAI = Kaimaninseln, KAN = Kanalinseln, KAS =
    Kasachstan, KIB = Kiribati, KIS = Kirgisistan, KOM = Komoren, KOR = Korea, Demokratische
    Volksrepublik (Nordkorea), KOS = Kosovo, KWT = Kuwait, L = Luxemburg, LAO = Laos, LAR = Libyen, LB =
    Liberia, LS = Lesotho, LT = Litauen, LV = Lettland, M = Malta, MA = Marokko, MAC = Macau, MAL =
    Malaysia, MAN = Insel Man, MAO = Oman, MAR = Marshallinseln, MAT = Martinique, MAY = Mayotte, MC =
    Monaco, MD = Moldau, MEX = Mexiko, MF = St.Martin (französischer Teil), MIK = Mikronesien, MK =
    Nordmazedonien, MNE = Montenegro, MON = Mongolei, MOT = Montserrat, MOZ = Mosambik, MS = Mauritius,
    MW = Malawi, MYA = Myanmar, N = Norwegen, NAU = Nauru, NEP = Nepal, NF = Norfolkinseln, NIC =
    Nicaragua, NIU = Niue, NKA = Neukaledonien, NL = Niederlande, NLA = Niederländische Antillen, NMA =
    Nördliche Marianen, NZ = Neuseeland, P = Portugal, PA = Panama, PAL = Palau, PE = Peru, PIE =
    St.Pierre und Miquelon, PIT = Pitcairninseln, PK = Pakistan, PL = Polen, PNG = Papua-Neuguinea, PRI
    = Puerto Rico, PSE = Palästinensische Gebiete, PY = Paraguay, QAT = Katar, RA = Argentinien, RB =
    Botsuana, RCA = Zentralafrikanische Republik, RCB = Kongo, RCH = Chile, REU = Réunion, RG = Guinea,
    RH = Haiti, RI = Indonesien, RIM = Mauretanien, RL = Libanon, RM = Madagaskar, RMM = Mali, RN =
    Niger, RO = Rumänien, ROK = Korea, Republik (Südkorea), ROU = Uruguay, RP = Philippinen, RSM = San
    Marino, RU = Burundi, RUS = Russische Föderation, RWA = Ruanda, S = Schweden, SAU = Saudi-Arabien,
    SCG = Serbien und Montenegro, SCN = St.Kitts und Nevis, SDN = Sudan, SGP = Singapur, SJ = Svalbard
    und Jan Mayen, SK = Slowakei, SLO = Slowenien, SME = Suriname, SN = Senegal, SOL = Salomonen, SP =
    Somalia, SRB = Serbien, SSD = Südsudan, STP = São Tomé und Príncipe, SWA =, SWZ = Namibia Eswatini,
    SY = Seychellen, SYR = Syrien, SX = St.Martin (niederländischer Teil), T = Thailand, TAD =
    Tadschikistan, TF = Französische Süd- und Antarktisgebiete, TG = Togo, TJ = China, TN = Tunesien,
    TOK = Tokelau, TON = Tonga, TR = Türkei, TT = Trinidad und Tobago, TUC = Turks- und Caicosinseln,
    TUR = Turkmenistan, TUV = Tuvalu, TWN = Taiwan, UA = Ukraine, UAE = Vereinigte Arabische Emirate, UM
    = Navassa / kleinere amerikanische Überseeinseln, USA = Vereinigte Staaten, USB = Usbekistan, V =
    Vatikanstadt, VAN = Vanuatu, VN = Vietnam, WAG = Gambia, WAL = Sierra Leone, WAN = Nigeria, WD =
    Dominica, WF = Wallis und Futuna, WG = Grenada, WL = St.Lucia, WS = Samoa, WV = St.Vincent und die
    Grenadinen, YEM = Jemen, YU = Jugoslawien, YV = Venezuela, Z = Sambia, ZA = Südafrika, ZRE = Kongo,
    Demokratische Republik, ZW = Simbabwe     |
    |  |   |
    | **nationality**   |   000 = Deutschland, 121 = Albanien, 122 = Bosnien und Herzegowina, 123 =
    Andorra, 124 = Belgien, 125 = Bulgarien, 126 = Dänemark, 127 = Estland, 128 = Finnland, 129 =
    Frankreich, 130 = Kroatien, 131 = Slowenien, 132 = Serbien und Montenegro, 133 = Serbien (einschl.
    Kosovo), 134 = Griechenland, 135 = Irland, 136 = Island, 137 = Italien, 138 = Jugoslawien, 139 =
    Lettland, 140 = Montenegro, 141 = Liechtenstein, 142 = Litauen, 143 = Luxemburg, 144 =
    Nordmazedonien, 145 = Malta, 146 = Moldau, 147 = Monaco, 148 = Niederlande, 149 = Norwegen, 150 =
    Kosovo, 151 = Österreich, 152 = Polen, 153 = Portugal, 154 = Rumänien, 155 = Slowakei, 156 = San
    Marino, 157 = Schweden, 158 = Schweiz, 160 = Russische Föderation, 161 = Spanien, 163 = Türkei, 164
    = Tschechien, 165 = Ungarn, 166 = Ukraine, 167 = Vatikanstadt, 168 = Vereinigtes Königreich , 169 =
    Weissrussland, 170 = Serbien, 181 = Zypern, 195 = Gibraltar, 199 = Übriges Europa, 221 = Algerien,
    223 = Angola, 224 = Eritrea, 225 = Äthiopien, 226 = Lesotho, 227 = Botsuana, 229 = Benin, 230 =
    Dschibuti, 231 = Côte d‘Ivoire, 232 = Nigeria, 233 = Simbabwe, 236 = Gabun, 237 = Gambia, 238 =
    Ghana, 239 = Mauretanien, 242 = Cabo Verde, 243 = Kenia, 244 = Komoren, 245 = Kongo, 246 = Kongo,
    Demokratische Republik, 247 = Liberia, 248 = Libyen, 249 = Madagaskar, 251 = Mali, 252 = Marokko,
    253 = Mauritius, 254 = Mosambik, 255 = Niger, 256 = Malawi, 257 = Sambia, 258 = Burkina Faso, 259 =
    Guinea-Bissau, 261 = Guinea, 262 = Kamerun, 263 = Südafrika, 265 = Ruanda, 267 = Namibia, 268 = São
    Tomé und Príncipe, 269 = Senegal, 271 = Seychellen, 272 = Sierra Leone, 273 = Somalia, 274 =
    Äquatorialguinea, 276 = Sudan (vor der Teilung des Landes), 277 = Sudan, 278 = Südsudan, 281 =
    Eswatini, 282 = Tansania, 283 = Togo, 284 = Tschad, 285 = Tunesien, 286 = Uganda, 287 = Ägypten, 289
    = Zentralafrikanische Republik, 291 = Burundi, 295 = Britisch abhängige Gebiete in Afrika, 299 =
    Übriges Afrika, 320 = Antigua und Barbuda, 322 = Barbados, 323 = Argentinien, 324 = Bahamas, 326 =
    Bolivien, 327 = Brasilien, 328 = Guyana, 330 = Belize, 332 = Chile, 333 = Dominica, 334 = Costa
    Rica, 335 = Dominikanische Republik, 336 = Ecuador, 337 = El Salvador, 340 = Grenada, 345 =
    Guatemala, 346 = Haiti, 347 = Honduras, 348 = Kanada, 349 = Kolumbien, 351 = Kuba, 353 = Mexiko, 354
    = Nicaragua, 355 = Jamaika, 357 = Panama, 359 = Paraguay, 361 = Peru, 364 = Suriname, 365 = Uruguay,
    366 = St. Lucia, 367 = Venezuela, 368 = Vereinigte Staaten, 369 = St. Vincent und die Grenadinen,
    370 = St. Kitts und Nevis, 371 = Trinidad und Tobago, 395 = Britisch abhängige Gebiete in Amerika,
    399 = Übriges Amerika, 411 = Hongkong, 412 =  Macau, 421 = Jemen, 422 = Armenien, 423 = Afghanistan,
    424 = Bahrain, 425 = Aserbaidschan, 426 = Bhutan, 427 = Myanmar, 429 = Brunei Darussalam, 430 =
    Georgien, 431 = Sri Lanka, 432 = Vietnam, 434 = Korea, Demokratische Volksrepublik (Nordkorea), 436
    = Indien, 437 = Indonesien, 438 = Irak, 439 = Iran, 441 = Israel, 442 = Japan, 444 = Kasachstan, 445
    = Jordanien, 446 = Kambodscha, 447 = Katar, 448 = Kuwait, 449 = Laos, 450 = Kirgisistan, 451 =
    Libanon, 454 = Malediven, 456 = Oman, 457 = Mongolei, 458 = Nepal, 459 = Palästinensische Gebiete,
    460 = Bangladesch, 461 = Pakistan, 462 = Philippinen, 465 = Taiwan, 467 = Korea, Republik
    (Südkorea), 469 = Vereinigte Arabische Emirate, 470 = Tadschikistan, 471 = Turkmenistan, 472 =
    Saudi-Arabien, 474 = Singapur, 475 = Syrien, 476 = Thailand, 477 = Usbekistan, 479 = China, 482 =
    Malaysia, 499 = Übriges Asien, 523 = Australien, 524 = Salomonen, 525 = Nördliche Marianen, 526 =
    Fidschi, 530 = Kiribati, 531 = Nauru, 532 = Vanuatu, 536 = Neuseeland, 537 = Palau, 538 = Papua-
    Neuguinea, 540 = Tuvalu, 541 = Tonga, 543 = Samoa, 544 = Marshallinseln, 545 = Mikronesien, 595 =
    Britisch abh. Gebiete in Australien/Ozeanien, 599 = Übriges Ozeanien, 996 = Unbekanntes Ausland, 997
    = staatenlos, 998 = ungeklärt, 999 = ohne Angabe    |
    |  |   |
    | **contribution_class_health_insurance**   |    0 = kein Beitrag (private KV oder frw. KV als
    Selbstzahler), 1 = allgemeiner Beitrag, 3 = ermäßigter Beitrag, 4 = Beitrag zur landwirtschaftlichen
    KV, 5 = Arbeitgeberbeitrag zur landwirtschaftlichen KV, 6 = Pauschalbeitrag für geringfügig
    Beschäftigte, 9 = Firmenzahler    |
    | **contribution_class_pension_insurance**   |   0 = kein Beitrag, 1 = voller Beitrag, 3 = halber
    Beitrag, 5 = Pauschalbeitrag für geringfügig Beschäftigte     |
    | **contribution_class_unemployment_insurance**   |    0 = kein Beitrag zur BA, 1 = voller Beitrag
    zur BA, 2 = halber Beitrag zur BA    |
    | **contribution_class_long_term_care_insurance**   |   0 = kein Beitrag zur gesetzl. PV, 1 = voller
    Beitrag zur gesetzl. PV, 2 = halber Beitrag zur gesetzl. PV    |
    | **person_group_key**   |  Lodas:  0 = keine Angabe, 101 = Sozialversicherungspflichtig
    Beschäftigte ohne besondere Merkmale, 102 = Auszubildende ohne besondere Merkmale, 103 =
    Beschäftigte in Altersteilzeit, 104 = Hausgewerbetreibende ( nicht Heimarbeiter ), 105 =
    Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in anerkannten Werkstätten oder
    gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109 = Geringfügig entlohnte
    Beschäftigte nach §8Abs.1 Nr.1 SGB IV, 110 = Kurzfristig Beschäftigte nach §8Abs.1 Nr.2 SGB IV, 111
    = Personen in Berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige
    in der Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal
    beschäftigt, 116 = Ausgleichsgeldempfänger nach dem FELEG, 118 = Unständig Beschäftigte, 119 =
    Versicherungsfr. Altersvollrentner/Versorgungsbezieher wg. Alters, 120 = Versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 121 = Auszubildende, deren Arbeitsentgelt die
    Geringverdienergrenze nicht übersteigt, 122 = Auszubildende in einer außerbetrieblichen Einrichtung,
    123 = Personen, die ein freiwilliges soziales oder ökologisches Jahr oder BFD leisten, 124 =
    Heimarbeiter ohne Entgeltfortzahlungsanspruch, 127 = Behinderte Menschen, die in einem
    Integrationsprojekt beschäftigt sind, 140 = Seeleute, 141 = Auszubildende in der Seefahrt (mit
    Arbeitsentgelt), 142 = Seeleute in Altersteilzeit, 143 = Seelotsen, 144 = Auszubildende in der
    Seefahrt, Arbeitsentgelt bis zur Geringverdienergrenze, 149 = In Seefahrt besch. versicherungsfr.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 150 = In Seefahrt besch. versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 190 = Beschäftigte, die nur in der gesetzlichen
    Unfallversicherung versichert sind  |
    |                        |  Lohn und Gehalt:  101 = Sozialversicherungspflichtig Beschäftigte, 102 =
    Auszubildende ohne besondere Merkmale, 103 = Beschäftigte in Altersteilzeit, 104 =
    Hausgewerbetreibende, 105 = Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in
    anerkannten Werkstätten oder gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109
    = Geringfügig entlohnte Beschäftigte, 110 = Kurzfristig Beschäftigte, 111 = Personen in
    berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige in der
    Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal beschäftigt, 116
    = Ausgleichsgeldempfänger nach dem FELEG, 118 = Berufsmäßig unständig Beschäftigte, 119 =
    Versicherungsfreie Altersvollrentner und Versorgungsbezieher wegen Alters, 120 =
    Versicherungspflichtige Altersvollrentner, 140 = Seeleute, 141 = Auszubildende in der Seefahrt, 142
    = Seeleute in Altersteilzeit, 143 = Seelotsen, 900 = Nicht meldepflichtig Beschäftigte, 127 =
    Behinderte Menschen, die in einem Integrationsprojekt beschäftigt sind, 190 = Beschäftigte, die nur
    in der gesetzlichen Unfallversicherung versichert sind, 144 = Auszubildende in der Seefahrt,
    Arbeitsentgelt bis zur Geringverdienergrenze, 123 = Personen, die ein freiwilliges soziales oder
    ökologisches Jahr oder BFD leisten, 122 = Auszubildende in einer außerbetrieblichen Einrichtung, 121
    = Auszubildende, deren Arbeitsentgelt die Geringverdienergrenze nicht übersteigt, 149 =
    Versicherungsfreie Altersvollrentner in der Seefahrt und Versorgungsbezieher, 124 = Heimarbeiter
    ohne Entgeltfortzahlungsanspruch, 117 = Nicht berufsmäßig unständig Beschäftigte, |
    |  |   |
    | **occupational_classification_code** | Ausgeübte Tätigkeit siehe:
    https://www.arbeitsagentur.de/datei/dok_ba015567.pdf   |
    | **occupational_classification_code_employee_leasing** | 0 = Keine_Angabe, 1 = nein, 2 = ja  |
    | **type_of_contract** |  0 = Keine_Angabe, 1 = Unbefristet in Vollzeit, 2 = Unbefristet in
    Teilzeit, 3 = Befristet in Vollzeit, 4 = Befristet in Teilzeit |
    |  |   |
    | **highest_level_of_professional_training** | 0 = Keine_Angabe, 1 = Ohne Ausbildungsabschluss, 2 =
    Ausbildungsabschluss, 3 = Meister, 4 = Bachelor, 5 = Diplom, 6 = Promotion, 9 = Abschluss unbekannt
    |
    | **highest_level_of_education** | 0 = Keine_Angabe, 1 = Ohne Schulabschluss, 2 =
    Hauptschulabschluss, 3 = Mittlere Reife, 4 = Abitur, 9 = Abschluss unbekannt  |
    | **is_ignore_additional_contribution_to_long_term_care_insurance_for_childless** | 0 = Nein, 1 = Ja
    |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]]:
    """ Get the list of employees' masterdata

     Masterdata of all employees can be accessed by the client's client-id.



     If a non-mandatory field is not filled in the payroll system, the field will not be exported
    through the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **sex**   |  Lodas: 0 = männlich, 1 = weiblich, 2 = divers, 3 = unbestimmt  |
    |           |  Lohn und Gehalt: 0 = weiblich, 1 = männlich, 2 = divers, 3 = unbestimmt |
    | **denomination/spouses_denomination**  |  Lodas:  0 = Konfessionslos / Keine
    Kirchensteuerberechnung, 1 = ev - Evangelische Kirchensteuer, 2 = rk - Römisch-Katholische
    Kirchensteuer, 3 = ak - Altkatholische Kirchensteuer, 4 = fa - Freie Religionsgemeinschaft Alzey, 5
    = fb - Freireligiöse Landesgemeinde Baden, 6 = fg - Freireligiöse Landesgemeinde Pfalz, 7 = fm -
    Freireligiöse Gemeinde Mainz, 8 = fr - Französisch reformiert (bis 12/2015), 9 = fs - Freireligiöse
    Gemeinde Offenbach/Main, 10 = ib - Israelitische Religionsgemeinschaft Baden, 11 = ih - Jüdische
    Kultussteuer, 12 = il - Israelitische Kultussteuer der kultusberechtigten Gemeinden, 13 = is -
    Israelitische / Jüdische Kultussteuer, 14 = iw - Israelitische Religionsgemeinschaft Württembergs,
    15 = jd - Jüdische Kultussteuer, 16 = jh - Jüdische Kultussteuer, 17 = lt - Evangelisch lutherisch
    (bis 12/2015), 18 = rf - Evangelisch reformiert (bis 12/2015) |
    |                    |  Lohn und Gehalt:  00 = Konfessionslos / Keine Kirchensteuerberechnung , 01 =
    rk - Römisch-Katholische Kirchensteuer, 02 = ev - Evangelische Kirchensteuer, 03 = lt - Evangelisch
    lutherisch (bis 12/2015), 04 = rf - Evangelisch reformiert (bis 12/2015), 05 = ak - Altkatholische
    Kirchensteuer, 06 = is - Israelitische / Jüdische Kultussteuer, 07 = fb - Freireligiöse
    Landesgemeinde Baden, 08 = ib - Israelitische Religionsgemeinschaft Baden, 09 = fo - Freireligiöse
    Gemeinde Offenbach/Main, 10 = fp - Freireligiöse Landesgemeinde Pfalz, 11 = fm - Freireligiöse
    Gemeinde Mainz, 12 = jü - Jüdisch, 13 = iw - Israelitische Religionsgemeinschaft Württembergs, 14 =
    if - Israelitische Kultussteuer Frankfurt, 15 = il - Israelitische Kultussteuer der
    kultusberechtigten Gemeinden, 16 = un - Unitarische Religionsgem. Freie Protestanten, 17 = fr -
    Französisch reformiert (bis 12/2015), 18 = fa - Freie Religionsgemeinschaft Alzey, 20 = fg -
    Freireligiöse Landesgemeinde Pfalz, 24 = jh - Jüdische Kultussteuer, 23 = jd - Jüdische
    Kultussteuer, 22 = ih - Jüdische Kultussteuer, 21 = fs - Freireligiöse Gemeinde Offenbach/Main
     |
    | **country**   |  0 = keine Angabe, A = Österreich, AFG = Afghanistan, AGO = Angola, AJ =
    Amerikanische Jungferninseln, AL = Albanien, AND = Andorra, ANG = Anguilla, ANT = Antigua und
    Barbuda, AQ = Antarktische Territorien, AQU = Äquatorialguinea, ARM = Armenien, AS = Amerikanisch
    Samoa, ASE = Aserbaidschan, AU = Korallenmeer-, Ashmore- und Cartierinseln, AUS = Australien, AW =
    Aruba, AX = Åland, B = Belgien, BD = Bangladesch, BDS = Barbados, BER = Bermuda, BG = Bulgarien, BH
    = Belize, BHT = Bhutan, BIH = Bosnien und Herzegowina, BIO = Malediven, BJ = Britische
    Jungferninseln, BL = St.Barthélemy, BOL = Bolivien, BQ = Bonaire, Saba, St.Eustatius, BR =
    Brasilien, BRN = Bahrain, BRU = Brunei Darussalam, BS = Bahamas, BV = Bouvetinsel, BY =
    Weissrussland, C = Kuba, CAM = Kamerun, CC = Kokosinseln, CDN = Kanada, CH = Schweiz, CHD = Tschad,
    CI = Côte d‘Ivoire, CL = Sri Lanka, CO = Kolumbien, COI = Cookinseln, CP = Clipperton, CR = Costa
    Rica, CV = Cabo Verde, CW = Curaçao, CY = Zypern, CX = Weihnachtsinsel, CZ = Tschechien, DK =
    Dänemark, DOM = Dominikanische Republik, DSC = Dschibuti, DY = Benin, DZ = Algerien, E = Spanien,
    EAK = Kenia, EAT = Tansania, EAU = Uganda, EC = Ecuador, EH = Westsahara, ERI = Eritrea, ES = El
    Salvador, EST = Estland, ET = Ägypten, ETH = Äthiopien, F = Frankreich, FAL = Falklandinseln, FG =
    Französisch Guayana, FIN = Finnland, FJI = Fidschi, FL = Liechtenstein, FP = Franz.-Polynesien, FR =
    Färöer, GAB = Gabun, GB = Vereinigtes Königreich, GCA = Guatemala, GEO = Georgien, GG = Guernsey, GH
    = Ghana, GIB = Gibraltar, GR = Griechenland, GRO = Grönland, GS = Südgeorgien und die südlichen
    Sandwichinseln, GUA = Guadeloupe, GUB = Guinea-Bissau, GUM = Guam, GUY = Guyana, H = Ungarn, HCA =
    Honduras, HEL = St. Helena /Ascension / Tristan da Cunha, HKG = Hongkong, HR = Kroatien, HM = Heard
    und McDonaldinseln, HV = Burkina Faso, I = Italien, IL = Israel, IND = Indien, IR = Iran, IRL =
    Irland, IRQ = Irak, IS = Island, IO = Britisches Territorium im Indischen Ozean, J = Japan, JA =
    Jamaika, JE = Jersey, JOR = Jordanien, K = Kambodscha, KAI = Kaimaninseln, KAN = Kanalinseln, KAS =
    Kasachstan, KIB = Kiribati, KIS = Kirgisistan, KOM = Komoren, KOR = Korea, Demokratische
    Volksrepublik (Nordkorea), KOS = Kosovo, KWT = Kuwait, L = Luxemburg, LAO = Laos, LAR = Libyen, LB =
    Liberia, LS = Lesotho, LT = Litauen, LV = Lettland, M = Malta, MA = Marokko, MAC = Macau, MAL =
    Malaysia, MAN = Insel Man, MAO = Oman, MAR = Marshallinseln, MAT = Martinique, MAY = Mayotte, MC =
    Monaco, MD = Moldau, MEX = Mexiko, MF = St.Martin (französischer Teil), MIK = Mikronesien, MK =
    Nordmazedonien, MNE = Montenegro, MON = Mongolei, MOT = Montserrat, MOZ = Mosambik, MS = Mauritius,
    MW = Malawi, MYA = Myanmar, N = Norwegen, NAU = Nauru, NEP = Nepal, NF = Norfolkinseln, NIC =
    Nicaragua, NIU = Niue, NKA = Neukaledonien, NL = Niederlande, NLA = Niederländische Antillen, NMA =
    Nördliche Marianen, NZ = Neuseeland, P = Portugal, PA = Panama, PAL = Palau, PE = Peru, PIE =
    St.Pierre und Miquelon, PIT = Pitcairninseln, PK = Pakistan, PL = Polen, PNG = Papua-Neuguinea, PRI
    = Puerto Rico, PSE = Palästinensische Gebiete, PY = Paraguay, QAT = Katar, RA = Argentinien, RB =
    Botsuana, RCA = Zentralafrikanische Republik, RCB = Kongo, RCH = Chile, REU = Réunion, RG = Guinea,
    RH = Haiti, RI = Indonesien, RIM = Mauretanien, RL = Libanon, RM = Madagaskar, RMM = Mali, RN =
    Niger, RO = Rumänien, ROK = Korea, Republik (Südkorea), ROU = Uruguay, RP = Philippinen, RSM = San
    Marino, RU = Burundi, RUS = Russische Föderation, RWA = Ruanda, S = Schweden, SAU = Saudi-Arabien,
    SCG = Serbien und Montenegro, SCN = St.Kitts und Nevis, SDN = Sudan, SGP = Singapur, SJ = Svalbard
    und Jan Mayen, SK = Slowakei, SLO = Slowenien, SME = Suriname, SN = Senegal, SOL = Salomonen, SP =
    Somalia, SRB = Serbien, SSD = Südsudan, STP = São Tomé und Príncipe, SWA =, SWZ = Namibia Eswatini,
    SY = Seychellen, SYR = Syrien, SX = St.Martin (niederländischer Teil), T = Thailand, TAD =
    Tadschikistan, TF = Französische Süd- und Antarktisgebiete, TG = Togo, TJ = China, TN = Tunesien,
    TOK = Tokelau, TON = Tonga, TR = Türkei, TT = Trinidad und Tobago, TUC = Turks- und Caicosinseln,
    TUR = Turkmenistan, TUV = Tuvalu, TWN = Taiwan, UA = Ukraine, UAE = Vereinigte Arabische Emirate, UM
    = Navassa / kleinere amerikanische Überseeinseln, USA = Vereinigte Staaten, USB = Usbekistan, V =
    Vatikanstadt, VAN = Vanuatu, VN = Vietnam, WAG = Gambia, WAL = Sierra Leone, WAN = Nigeria, WD =
    Dominica, WF = Wallis und Futuna, WG = Grenada, WL = St.Lucia, WS = Samoa, WV = St.Vincent und die
    Grenadinen, YEM = Jemen, YU = Jugoslawien, YV = Venezuela, Z = Sambia, ZA = Südafrika, ZRE = Kongo,
    Demokratische Republik, ZW = Simbabwe     |
    |  |   |
    | **nationality**   |   000 = Deutschland, 121 = Albanien, 122 = Bosnien und Herzegowina, 123 =
    Andorra, 124 = Belgien, 125 = Bulgarien, 126 = Dänemark, 127 = Estland, 128 = Finnland, 129 =
    Frankreich, 130 = Kroatien, 131 = Slowenien, 132 = Serbien und Montenegro, 133 = Serbien (einschl.
    Kosovo), 134 = Griechenland, 135 = Irland, 136 = Island, 137 = Italien, 138 = Jugoslawien, 139 =
    Lettland, 140 = Montenegro, 141 = Liechtenstein, 142 = Litauen, 143 = Luxemburg, 144 =
    Nordmazedonien, 145 = Malta, 146 = Moldau, 147 = Monaco, 148 = Niederlande, 149 = Norwegen, 150 =
    Kosovo, 151 = Österreich, 152 = Polen, 153 = Portugal, 154 = Rumänien, 155 = Slowakei, 156 = San
    Marino, 157 = Schweden, 158 = Schweiz, 160 = Russische Föderation, 161 = Spanien, 163 = Türkei, 164
    = Tschechien, 165 = Ungarn, 166 = Ukraine, 167 = Vatikanstadt, 168 = Vereinigtes Königreich , 169 =
    Weissrussland, 170 = Serbien, 181 = Zypern, 195 = Gibraltar, 199 = Übriges Europa, 221 = Algerien,
    223 = Angola, 224 = Eritrea, 225 = Äthiopien, 226 = Lesotho, 227 = Botsuana, 229 = Benin, 230 =
    Dschibuti, 231 = Côte d‘Ivoire, 232 = Nigeria, 233 = Simbabwe, 236 = Gabun, 237 = Gambia, 238 =
    Ghana, 239 = Mauretanien, 242 = Cabo Verde, 243 = Kenia, 244 = Komoren, 245 = Kongo, 246 = Kongo,
    Demokratische Republik, 247 = Liberia, 248 = Libyen, 249 = Madagaskar, 251 = Mali, 252 = Marokko,
    253 = Mauritius, 254 = Mosambik, 255 = Niger, 256 = Malawi, 257 = Sambia, 258 = Burkina Faso, 259 =
    Guinea-Bissau, 261 = Guinea, 262 = Kamerun, 263 = Südafrika, 265 = Ruanda, 267 = Namibia, 268 = São
    Tomé und Príncipe, 269 = Senegal, 271 = Seychellen, 272 = Sierra Leone, 273 = Somalia, 274 =
    Äquatorialguinea, 276 = Sudan (vor der Teilung des Landes), 277 = Sudan, 278 = Südsudan, 281 =
    Eswatini, 282 = Tansania, 283 = Togo, 284 = Tschad, 285 = Tunesien, 286 = Uganda, 287 = Ägypten, 289
    = Zentralafrikanische Republik, 291 = Burundi, 295 = Britisch abhängige Gebiete in Afrika, 299 =
    Übriges Afrika, 320 = Antigua und Barbuda, 322 = Barbados, 323 = Argentinien, 324 = Bahamas, 326 =
    Bolivien, 327 = Brasilien, 328 = Guyana, 330 = Belize, 332 = Chile, 333 = Dominica, 334 = Costa
    Rica, 335 = Dominikanische Republik, 336 = Ecuador, 337 = El Salvador, 340 = Grenada, 345 =
    Guatemala, 346 = Haiti, 347 = Honduras, 348 = Kanada, 349 = Kolumbien, 351 = Kuba, 353 = Mexiko, 354
    = Nicaragua, 355 = Jamaika, 357 = Panama, 359 = Paraguay, 361 = Peru, 364 = Suriname, 365 = Uruguay,
    366 = St. Lucia, 367 = Venezuela, 368 = Vereinigte Staaten, 369 = St. Vincent und die Grenadinen,
    370 = St. Kitts und Nevis, 371 = Trinidad und Tobago, 395 = Britisch abhängige Gebiete in Amerika,
    399 = Übriges Amerika, 411 = Hongkong, 412 =  Macau, 421 = Jemen, 422 = Armenien, 423 = Afghanistan,
    424 = Bahrain, 425 = Aserbaidschan, 426 = Bhutan, 427 = Myanmar, 429 = Brunei Darussalam, 430 =
    Georgien, 431 = Sri Lanka, 432 = Vietnam, 434 = Korea, Demokratische Volksrepublik (Nordkorea), 436
    = Indien, 437 = Indonesien, 438 = Irak, 439 = Iran, 441 = Israel, 442 = Japan, 444 = Kasachstan, 445
    = Jordanien, 446 = Kambodscha, 447 = Katar, 448 = Kuwait, 449 = Laos, 450 = Kirgisistan, 451 =
    Libanon, 454 = Malediven, 456 = Oman, 457 = Mongolei, 458 = Nepal, 459 = Palästinensische Gebiete,
    460 = Bangladesch, 461 = Pakistan, 462 = Philippinen, 465 = Taiwan, 467 = Korea, Republik
    (Südkorea), 469 = Vereinigte Arabische Emirate, 470 = Tadschikistan, 471 = Turkmenistan, 472 =
    Saudi-Arabien, 474 = Singapur, 475 = Syrien, 476 = Thailand, 477 = Usbekistan, 479 = China, 482 =
    Malaysia, 499 = Übriges Asien, 523 = Australien, 524 = Salomonen, 525 = Nördliche Marianen, 526 =
    Fidschi, 530 = Kiribati, 531 = Nauru, 532 = Vanuatu, 536 = Neuseeland, 537 = Palau, 538 = Papua-
    Neuguinea, 540 = Tuvalu, 541 = Tonga, 543 = Samoa, 544 = Marshallinseln, 545 = Mikronesien, 595 =
    Britisch abh. Gebiete in Australien/Ozeanien, 599 = Übriges Ozeanien, 996 = Unbekanntes Ausland, 997
    = staatenlos, 998 = ungeklärt, 999 = ohne Angabe    |
    |  |   |
    | **contribution_class_health_insurance**   |    0 = kein Beitrag (private KV oder frw. KV als
    Selbstzahler), 1 = allgemeiner Beitrag, 3 = ermäßigter Beitrag, 4 = Beitrag zur landwirtschaftlichen
    KV, 5 = Arbeitgeberbeitrag zur landwirtschaftlichen KV, 6 = Pauschalbeitrag für geringfügig
    Beschäftigte, 9 = Firmenzahler    |
    | **contribution_class_pension_insurance**   |   0 = kein Beitrag, 1 = voller Beitrag, 3 = halber
    Beitrag, 5 = Pauschalbeitrag für geringfügig Beschäftigte     |
    | **contribution_class_unemployment_insurance**   |    0 = kein Beitrag zur BA, 1 = voller Beitrag
    zur BA, 2 = halber Beitrag zur BA    |
    | **contribution_class_long_term_care_insurance**   |   0 = kein Beitrag zur gesetzl. PV, 1 = voller
    Beitrag zur gesetzl. PV, 2 = halber Beitrag zur gesetzl. PV    |
    | **person_group_key**   |  Lodas:  0 = keine Angabe, 101 = Sozialversicherungspflichtig
    Beschäftigte ohne besondere Merkmale, 102 = Auszubildende ohne besondere Merkmale, 103 =
    Beschäftigte in Altersteilzeit, 104 = Hausgewerbetreibende ( nicht Heimarbeiter ), 105 =
    Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in anerkannten Werkstätten oder
    gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109 = Geringfügig entlohnte
    Beschäftigte nach §8Abs.1 Nr.1 SGB IV, 110 = Kurzfristig Beschäftigte nach §8Abs.1 Nr.2 SGB IV, 111
    = Personen in Berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige
    in der Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal
    beschäftigt, 116 = Ausgleichsgeldempfänger nach dem FELEG, 118 = Unständig Beschäftigte, 119 =
    Versicherungsfr. Altersvollrentner/Versorgungsbezieher wg. Alters, 120 = Versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 121 = Auszubildende, deren Arbeitsentgelt die
    Geringverdienergrenze nicht übersteigt, 122 = Auszubildende in einer außerbetrieblichen Einrichtung,
    123 = Personen, die ein freiwilliges soziales oder ökologisches Jahr oder BFD leisten, 124 =
    Heimarbeiter ohne Entgeltfortzahlungsanspruch, 127 = Behinderte Menschen, die in einem
    Integrationsprojekt beschäftigt sind, 140 = Seeleute, 141 = Auszubildende in der Seefahrt (mit
    Arbeitsentgelt), 142 = Seeleute in Altersteilzeit, 143 = Seelotsen, 144 = Auszubildende in der
    Seefahrt, Arbeitsentgelt bis zur Geringverdienergrenze, 149 = In Seefahrt besch. versicherungsfr.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 150 = In Seefahrt besch. versicherungspfl.
    Altersvollrentner/Versorgungsbezieher wg. Alters, 190 = Beschäftigte, die nur in der gesetzlichen
    Unfallversicherung versichert sind  |
    |                        |  Lohn und Gehalt:  101 = Sozialversicherungspflichtig Beschäftigte, 102 =
    Auszubildende ohne besondere Merkmale, 103 = Beschäftigte in Altersteilzeit, 104 =
    Hausgewerbetreibende, 105 = Praktikanten, 106 = Werkstudenten, 107 = Behinderte Menschen in
    anerkannten Werkstätten oder gleichartigen Einrichtungen, 108 = Bezieher von Vorruhestandsgeld, 109
    = Geringfügig entlohnte Beschäftigte, 110 = Kurzfristig Beschäftigte, 111 = Personen in
    berufsfördernden Maßnahmen zur Rehabilitation, 112 = Mitarbeitende Familienangehörige in der
    Landwirtschaft, 113 = Nebenerwerbslandwirte, 114 = Nebenerwerbslandwirte - saisonal beschäftigt, 116
    = Ausgleichsgeldempfänger nach dem FELEG, 118 = Berufsmäßig unständig Beschäftigte, 119 =
    Versicherungsfreie Altersvollrentner und Versorgungsbezieher wegen Alters, 120 =
    Versicherungspflichtige Altersvollrentner, 140 = Seeleute, 141 = Auszubildende in der Seefahrt, 142
    = Seeleute in Altersteilzeit, 143 = Seelotsen, 900 = Nicht meldepflichtig Beschäftigte, 127 =
    Behinderte Menschen, die in einem Integrationsprojekt beschäftigt sind, 190 = Beschäftigte, die nur
    in der gesetzlichen Unfallversicherung versichert sind, 144 = Auszubildende in der Seefahrt,
    Arbeitsentgelt bis zur Geringverdienergrenze, 123 = Personen, die ein freiwilliges soziales oder
    ökologisches Jahr oder BFD leisten, 122 = Auszubildende in einer außerbetrieblichen Einrichtung, 121
    = Auszubildende, deren Arbeitsentgelt die Geringverdienergrenze nicht übersteigt, 149 =
    Versicherungsfreie Altersvollrentner in der Seefahrt und Versorgungsbezieher, 124 = Heimarbeiter
    ohne Entgeltfortzahlungsanspruch, 117 = Nicht berufsmäßig unständig Beschäftigte, |
    |  |   |
    | **occupational_classification_code** | Ausgeübte Tätigkeit siehe:
    https://www.arbeitsagentur.de/datei/dok_ba015567.pdf   |
    | **occupational_classification_code_employee_leasing** | 0 = Keine_Angabe, 1 = nein, 2 = ja  |
    | **type_of_contract** |  0 = Keine_Angabe, 1 = Unbefristet in Vollzeit, 2 = Unbefristet in
    Teilzeit, 3 = Befristet in Vollzeit, 4 = Befristet in Teilzeit |
    |  |   |
    | **highest_level_of_professional_training** | 0 = Keine_Angabe, 1 = Ohne Ausbildungsabschluss, 2 =
    Ausbildungsabschluss, 3 = Meister, 4 = Bachelor, 5 = Diplom, 6 = Promotion, 9 = Abschluss unbekannt
    |
    | **highest_level_of_education** | 0 = Keine_Angabe, 1 = Ohne Schulabschluss, 2 =
    Hauptschulabschluss, 3 = Mittlere Reife, 4 = Abitur, 9 = Abschluss unbekannt  |
    | **is_ignore_additional_contribution_to_long_term_care_insurance_for_childless** | 0 = Nein, 1 = Ja
    |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, list['MasterData']]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )).parsed
