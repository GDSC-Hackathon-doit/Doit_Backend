from datetime import datetime
from database import SessionLocal
from crud import create_article
from schema import ArticleCreate
from models import Base
from database import engine



test_articles = [
{
"title":"금리 인상이 멈추자 장기채가 주목받고 있어요",
"subTitle":"미래에 금리가 내리면 채권 가격이 오를 테니, 그 시기를 대비하는 거예요.",
"description":"금리 상승세가 멈췄다는 얘기가 나오면서 만기가 긴 장기 채권이 유망한 투자처로 떠오르고 있어요. 지금 기준금리가 가장 높은 수준이라는 건 채권 가격이 낮다는 뜻이잖아요. 미래에 금리가 내리면 채권 가격이 오를 테니, 그 시기를 대비해 미리 장기채를 사두려는 수요가 많아진 거예요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-11",
"imgUrl":"https://static.toss.im/assets/finance-tips/img-longterm-bond.png",
"imgAlt":"금리 인상이 멈추자 장기채가 주목받고 있어요",
"publishedTime":"2023-04-28T07:25:00+09:00",
"click":None,
"like":None
},
{
"title":"조각투자가 뭐예요?",
"subTitle":"요즘 뜨는 조각투자, 기초 개념부터 알아보기 ",
"description":"조각투자라는 새로운 시장에 투자자들의 이목이 모이고 있어요. 조각투자란 여러 사람이 건물, 그림 등 하나의 자산을 잘게 나누어 사고 파는 것을 말해요. 피자 한 판을 조각내 여럿이 나눠 먹는 것처럼요. 3040 세대의 경제생활을 쉽고 친절하게 다루는 <경제전파사>와 함께 조각투자에 대해...",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/sto-01",
"imgUrl":"https://static.toss.im/illusts-content/img-inventing-piece.jpg",
"imgAlt":"부동산 조각투자 이미지입니다",
"publishedTime":"2023-04-27T16:53:00+09:00",
"click":None,
"like":None
},
{
"title":"내게 맞는 아파트 찾기",
"subTitle":"판상형, 타워형, 혼합형 중 무엇이 좋을까",
"description":"월세, 전세, 매매 무엇이든 집을 계약한다는 건 인생에서 큰일이죠. 이번 주제는 아파트 형태와 평면입니다. 거주지로 아파트를 고려하고 있다면, 판상형과 타워형, 혼합형의 특징과 차이를 꼭 살펴보세요. 도시계획 전문가 얼랩 저자가 설명해 드려요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/house-contract-19",
"imgUrl":"https://static.toss.im/ml-illusts-common/img-apartment-grid.jpg",
"imgAlt":"아파트에 관한 추상적인 그래픽",
"publishedTime":"2023-04-25T11:39:00+09:00",
"click":None,
"like":None
},
{
"title":"공급면적과 전용면적, 어떻게 다른가요? 분양 공고 용어 정리 ",
"subTitle":"입주자 모집 공고를 볼 때 헷갈리기 쉬운 용어들을 쉽게 풀어 알려드려요. ",
"description":"공급면적과 전용면적, 공용면적, 계약면적 뭐가 어떻게 다른 걸까요? 입주자 모집 공고를 처음 본다면 낯선 용어 때문에 당황하기 쉬운데요. 자주 나오는 단어인 만큼 눈에 익혀둬야 할 용어들을 쉽게 풀어 알려드릴게요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/housing_0424",
"imgUrl":"https://static.toss.im/ml-illusts-common/img-book-house.jpeg",
"imgAlt":"공급면적과 전용면적, 어떻게 다른가요? 분양 공고 용어 정리",
"publishedTime":"2023-04-24T23:01:00+09:00",
"click":None,
"like":None
},
{
"title":"⟨사소한 질문들⟩ 봄호: 저작권으로 먹고살기",
"subTitle":"모두가 창작자인 시대, 저작권에 대한 네가지 질문",
"description":"불안한 세상에서 소득 파이프라인을 하나라도 더 만드는 일은 너무나도 중요해졌습니다. 게다가 저작권으로 만든 파이프라인이라면, 저작권이 보장되는 70년 동안 비빌 언덕이 되어주는 거죠. 나도 저작권으로 먹고살 수 있을까요?",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/tinyquestions-copyright-0",
"imgUrl":"https://static.toss.im/illusts-content/img-tinyq-spring0-article.jpg",
"imgAlt":"연필, 음표가 그려진 지폐가 담겨있는 지갑 그래픽",
"publishedTime":"2023-04-24T10:04:00+09:00",
"click":None,
"like":None
},
{
"title":"나도 저작권으로 먹고살 수 있을까?",
"subTitle":"BTS 노래의 작사가, 48개 출시한 이모티콘 작가에게 물었습니다",
"description":"저작권으로 먹고사는 세상이 너무 궁금한 나머지 ① 이모티콘 작가 김소희를 찾아가 “이모티콘 하나 터지면 경제적 자유가 시작되는지”, ② 싱어송라이터 안복진을 찾아가 “BTS 노래 한 곡을 작사했으니 이제 먹고살 걱정이 없어졌는지” 묻고 말았습니다.",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/tinyquestions-copyright-1",
"imgUrl":"https://static.toss.im/illusts-content/img-tinyq-spring1-cover.png",
"imgAlt":"음표와 가격표가 있는 이모티콘들",
"publishedTime":"2023-04-24T10:03:00+09:00",
"click":None,
"like":None
},
{
"title":"웹소설 작가 연봉은 정말 1억일까?",
"subTitle":"<사내맞선> 원작자에게 듣는 웹소설로 먹고 살기",
"description":"혹시 꺼지지 않는 창작욕의 불씨를 품고 있거나, 연봉 1억을 만들어줄 웹소설 쓰기를 꿈꾸고 있다면 마음 단단히 먹고 글을 읽어주세요. 누구나 도전할 수 있지만 아무나 될 수 없는 웹소설 작가의 ‘결코 만만치 않은 세계'로 안내합니다.",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/tinyquestions-copyright-2",
"imgUrl":"https://static.toss.im/illusts-content/img-tinyq-spring2-cover.jpg",
"imgAlt":"레트로 타자기에서 나오는 1억 수표 그래픽",
"publishedTime":"2023-04-24T10:02:00+09:00",
"click":None,
"like":None
},
{
"title":"내가 만든 영상도 저작권을 보호받을 수 있을까?",
"subTitle":"시대에 따라 저작권도 변한다",
"description":"누군가 내 콘텐츠를 따라 하면 어떻게 해야할까요? 누구나 저작자가 될 수 있는 시대. 1인미디어/크리에이터의 저작권, 어떻게 보호되고 있는지 빠르게 변하는 시대에 따라 저작권법에는 어떤 변화가 있는지 살펴봅니다.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/tinyquestions-copyright-3",
"imgUrl":"https://static.toss.im/illusts-content/img-tinyq-spring3-cover.jpg",
"imgAlt":"도둑들이 영상의 내용을 훔치는 이미지",
"publishedTime":"2023-04-24T10:01:00+09:00",
"click":None,
"like":None
},
{
"title":"AI도 저작권을 가질 수 있을까?",
"subTitle":"인공지능과 함께 살아가기 위해 생각해 볼 것들",
"description":"AI 개발자 스테판 탈러(Stephen Thaler)는 미국 저작권청에 인공지능이 창작한 ‘파라다이스로 가는 최근 출입구’라는 이미지에 대해 저작권 등록 신청을 했다. 결과는 어땠을까?",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/tinyquestions-copyright-4",
"imgUrl":"https://static.toss.im/illusts-content/img-tinyq-spring4-cover.jpg",
"imgAlt":"미술 작품을 연상하는 프레임 속 프로그래밍 언어가 가득찬 이미지",
"publishedTime":"2023-04-24T10:00:00+09:00",
"click":None,
"like":None
},
{
"title":"하락장이 시작되면 사람들이 관심 갖는 상품은?",
"subTitle":"인버스 ETF와 곱버스 ETF",
"description":"주식 시장이 안 좋아지자 인버스 ETF와 곱버스 ETF가 인기를 끌고 있어요. ETF(상장지수펀드)는 주가 지수등을 따르는 펀드예요. 종목 하나에 투자하는 주식과 달리 주가 지수를 따르는 펀드를 주식시장에 상장시켜 투자하도록 하는 거죠. 그런데 인버스, 곱버스 ETF는 지수와 가격을 반대로 따라요.",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-10",
"imgUrl":"https://static.toss.im/illusts-content/img-etftech-cover.jpg",
"imgAlt":"하락장이 시작되면 사람들이 관심 갖는 상품은?",
"publishedTime":"2023-04-21T10:25:00+09:00",
"click":None,
"like":None
},
{
"title":"아이와 함께 경제 신문 읽기 가이드 ",
"subTitle":"‘첫 만남’ 준비하기부터 신문과 친해지는 방법까지 ",
"description":"수능 언어영역 지문에 경제 용어가 등장했기 때문일까요. 엄마, 아빠가 모인 커뮤니티에선 요즘 ‘문해력’ ‘경제신문’ 키워드가 자주 보여요. 토스 앱을 쓰는 자녀를 둔 부모님들에게도 아이와 함께 어린이 경제신문 읽기에 대해 궁금한 질문을 받아봤는데요. 100개가 넘는 질문들이 쏟아졌어요.",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/parents-money-study-5",
"imgUrl":"https://static.toss.im/illusts/img-finance-education-ep5.png",
"imgAlt":"아이와 함께 경제 신문 읽기 가이드",
"publishedTime":"2023-04-20T09:38:00+09:00",
"click":None,
"like":None
},
{
"title":"하루만 맡겨도 이자가 붙는 ‘파킹통장’이란?",
"subTitle":"파킹통장 이용할 때 알아두면 좋은 점",
"description":"지난해, 기준금리가 높아지면서 은행 수시 입출금 통장 대신 하루만 맡겨도 이자를 받을 수 있는 고금리 파킹통장에 대한 관심이 높아졌어요. 파킹통장은 parking(주차)와 통장의 합성어로, 차를 잠시 주차하듯 언제든지 돈을 넣었다 뺄 수 있는 통장이에요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-9",
"imgUrl":"https://static.toss.im/illusts-content/img-parkingacc-cover.jpg",
"imgAlt":"하루만 맡겨도 이자가 붙는 ‘파킹통장’이란?",
"publishedTime":"2023-04-19T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"중앙은행 디지털화폐(CBDC) 도입되면 바뀌는 것",
"subTitle":"다 지켜보는 중앙은행, 시중 은행은 역할 축소? ",
"description":"한국은행이 디지털화폐를 직접 발행하면 어떤 일이 벌어질까요? 중앙은행의 빅브라더화, 시중 은행의 역할 축소? 팬데믹과 함께 비대면 결제 서비스가 급속도로 확산되면서 중요성이 대두된 중앙은행 디지털화폐(CBDC)가 현실화되면 바뀌는 것을 예측해봤습니다.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/digital-asset-club-3",
"imgUrl":"https://static.toss.im/illusts-content/img-digitmoney-cover.jpg",
"imgAlt":"디지털화폐 이미지",
"publishedTime":"2023-04-18T16:30:00+09:00",
"click":None,
"like":None
},
{
"title":"가계부 비상전략 짜기, 나의 최저생활비는 얼마일까?",
"subTitle":"소득이 부족한 겨울을 버티는 비상 전략",
"description":"날씨에 봄, 여름, 가을, 겨울이 있듯 가계부에도 사계절이 있어요. 필요한 돈은 많은데 소득이 부족한 겨울이 오면 비상 전략이 필요하죠. ‘무조건 절약’으로 인한 피로감은 줄이면서 과소비를 막을 방법 중 하나는 나만의 최저생활비를 구해보는 거예요. 3개월 동안 가계부를 작성하면서 아래 항목을 정리하면 최서쟁활비 얼마인지 알 수 있어요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/zzantech-3",
"imgUrl":"https://static.toss.im/illusts/img-emergency-strategy.png",
"imgAlt":"가계부 비상전략 짜기, 나의 최저생활비는 얼마일까?",
"publishedTime":"2023-04-17T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"요즘 주목받는 아트테크, 시작해도 괜찮을까?",
"subTitle":"아트테크 투자하는 법과 주의할 점",
"description":"미술작품에 투자하는 아트테크가 떠오르고 있어요. 다만 시장이 형성된 지 얼마 되지 않아 우려의 목소리도 있기에에 주의깊게 살펴봐야 해요. 아트테크 시작할 수 있는 플랫폼과 주의할 점을 알려드려요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-8",
"imgUrl":"https://static.toss.im/illusts-content/img-artpuzzle-cover.jpg",
"imgAlt":"요즘 주목받는 아트테크, 시작해도 괜찮을까?",
"publishedTime":"2023-04-14T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"리볼빙, 모르고 쓰면 안 돼요",
"subTitle":"모르고 쓰면 안 되는 이유 3가지는?",
"description":"‘신용카드 결제금액이 평소보다 많이 나왔다' 싶으면 카드사에서 리볼빙 서비스를 추천하기도 해요. 리볼빙의 정식 명칭은 ‘일부결제금액이월약정’. 신용카드 결제금액의 일부만 먼저 갚고, 나머지는 나중으로 미뤄서 갚을 수 있는 서비스예요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/what-to-know-about-revolving",
"imgUrl":"https://static.toss-internal.com/ipd-tcs/toss_core/live/5a4e0494-39fd-4a08-ac12-af752ab41294.png",
"imgAlt":"리볼빙, 모르고 쓰면 안 돼요",
"publishedTime":"2023-04-14T02:59:00+09:00",
"click":None,
"like":None
},
{
"title":"“안 하면 손해?” 내가 묻지마 투자에 빠진 이유",
"subTitle":"냅다 투자하는 불나방, 벗어나고 싶다면",
"description":"관심 있는 주식 종목 그래프의 지나간 고점을 보고 냅다 매수를 감행하는 불나방에게도, 나 빼고 다들 하는 것 같아 불안해서 투자해볼까 기웃대는 개미에게도 이유는 있다. “투자할 때 내가 대체 왜 이럴까\" 싶었던 낙관과 불안의 심리를 전문가와 함께 파헤쳐보자.",
"hardness":0,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/cognitive-money-4",
"imgUrl":"https://static.toss.im/illusts-content/img-moneypieman-cover.jpg",
"imgAlt":"코앞만 바라보며 서있는 사람",
"publishedTime":"2023-04-13T09:26:00+09:00",
"click":None,
"like":None
},
{
"title":"분양받은 아파트, 이제 3년 지나면 팔 수 있어요",
"subTitle":"수도권은 분양 후 최대 3년, 비수도권은 최대 1년 이후 팔 수 있어요.",
"description":"아파트를 분양받은 후 최대 10년까지 팔지 못하게 하던 전매제한 규제가 2023년 4월 7일부터 풀렸어요. 수도권은 분양 후 최대 3년, 비수도권은 최대 1년 이후 팔 수 있게 돼요. 다만 실거주 의무는 아직 남아 있어요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/news-230407",
"imgUrl":"https://static.toss.im/illusts-content/img-housekey-cover.jpg",
"imgAlt":"분양받은 아파트, 이제 3년 지나면 팔 수 있어요",
"publishedTime":"2023-04-13T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"계속 변하는 환율, 달러 투자 괜찮을까?",
"subTitle":"달러 정기예금 금리를 확인해보세요.",
"description":"전문가들은 장기적으로 원-달러 환율이 하락세를 보일 거라는 전망을 내놓고 있는데요. 그럼에도 분산투자 측면에서 달러 투자를 추천하기도 해요. 달러가 올랐을 때 되팔아 돈을 버는 환차익만을 노리기보다 외화 정기예금 상품에 눈을 돌릴 필요가 있다고 조언하는 거예요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-07",
"imgUrl":"https://static.toss.im/illusts-content/img-dollar-invent.jpg",
"imgAlt":"계속 변하는 환율, 달러 투자 괜찮을까?",
"publishedTime":"2023-04-11T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"내 보험료 결정하는 특약, 똑똑하게 가입하는 법 ",
"subTitle":"하나의 보험 안에 넣을 수 있는 특약은 셀 수 없이 많아요. ",
"description":"나에게 반드시 필요한 특약이 무엇인지 알고 선택과 집중을 하는 것이 중요해요. 특약, 똑똑하게 가입하는 방법을 알려드려요. 여러가지 보장 중에서도 가장 우선순위를 높게 가져가면 좋은 5가지가 있어요. 이것만 잘 준비해도 우리가 살아가면서 마주칠 대부분의 큰 위험은 대비할 수 있어요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/insu-special-contract",
"imgUrl":"https://static.toss.im/illusts-content/img-paperman-cover.jpg",
"imgAlt":"보험료 결정하는 특약, 가입하는 방법",
"publishedTime":"2023-04-07T10:59:00+09:00",
"click":None,
"like":None
},
{
"title":"최근 MZ세대에서 주목받는 재테크는 리셀?",
"subTitle":"리셀테크 할 때 주의할 점 3가지",
"description":"리셀(Resell)은 되파는 행위를 말해요. MZ세대 사이에서는 수요가 많거나 희소성 있는 상품을 구한 뒤, 기존 가격에 프리미엄을 붙여 파는 리셀테크(리셀+재테크)가 유행이에요. 단순히 고가의 명품, 스니커즈 등만 리셀 되는 게 아니라 위스키 병, 명품 브랜드 쇼핑백, 명품 시계 브랜드 박스 등도 대상이 되면서 리셀테크 시장 규모가 1조 원에 이르고 있다고 해요.",
"hardness":2,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/high-interest-06",
"imgUrl":"https://static.toss.im/illusts-content/img-resell-cover.jpg",
"imgAlt":"최근 MZ세대에서 주목받는 재테크는 리셀?",
"publishedTime":"2023-04-07T08:00:00+09:00",
"click":None,
"like":None
},
{
"title":"레벨3. 가진 돈은 너무 작고 소중한데, 큰돈을 모으고 싶을 때",
"subTitle":"내 상황에 맞는 금융상품 고르고, 같은 돈으로 더 크게 불리는 방법",
"description":"용돈 좀 모아보려고 했는데 복잡한 금융 상품 앞에서 당황스러웠다면? 오늘은 내 상황에 맞게 금융상품 선택하는 방법과 적은 돈을 모아도 결국 큰 차이를 만드는 복리의 기적을 알려드릴게요.\n1) 콘서트 가려고 모으는 돈, 뭘 가입해야 될까? 2) 그냥 통장과 적금, 예금 구분하는 방법 3) 매월 1만원씩 저축했을 때 얼마 돌려받을까? 4) 용돈을 더 빨리 크게 불리는 방법",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/money-challenge-03",
"imgUrl":"https://static.toss.im/illusts/img-money-challenge-ep3.png",
"imgAlt":"3단계 머니챌린지 통장 이미지",
"publishedTime":"2023-04-06T12:05:00+09:00",
"click":None,
"like":None
},
{
"title":"일론 머스크가 한국에 새 회사를 연대요",
"subTitle":"주인공은 스타링크 코리아. 어떤 곳인지 알려드릴게요.",
"description":"주인공은 바로 무성인터넷 회사 '스타링크 코리아'. 일론 머스크는 테슬라가 그랬던 것처럼, 스타링크가 인터넷 사업에 새로운 혁신을 불러올 것이라는 자신감을 갖고 있어요. 스타링크는 어떤 곳인지, 한국에선 어떤 활동을 펼치게 될지 쉽고 재밌게 알려드릴게요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/starlinkkorea",
"imgUrl":"https://static.toss.im/illusts-content/img-cover-feed-starlink.png",
"imgAlt":"지구 위에서 무선인터넷이 발신되는 모양의 그래픽",
"publishedTime":"2023-04-04T18:50:00+09:00",
"click":None,
"like":None
},
{
"title":"공동구매 하면 왜 가격이 떨어질까?",
"subTitle":"내 소비임에도 나 혼자 결정하는 것이 아닌 이유",
"description":"내 소비임에도 나 혼자 결정하는 것이 아닌 이유. 다른 사람의 소비가 내 소비에 영향을 미친다면? 공동구매 할 때 가격이 떨어지는 이유, 명품 브랜드가 소비 욕구를 자극하는 방법, 리셀 현상이 일어나는 이유 모두 이해할 수 있어요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/group-purchase",
"imgUrl":"https://static.toss.im/illusts/img-everyday-economics-ep3.jpg",
"imgAlt":"공동구매",
"publishedTime":"2023-04-04T14:31:00+09:00",
"click":None,
"like":None
},
{
"title":"햇살론뱅크: 신용 낮은 사람이 1금융권 대출받는 법",
"subTitle":"금리는 연 2.9~6% 수준으로 저축은행이나 캐피탈 대출보다 훨씬 저렴해요.",
"description":"신용점수가 낮거나 소득이 낮으면 좋은 조건으로 대출받기 어렵죠. 이런 사람들이 너무 고금리로 대출을 받아 이자 부담이 높아지는 걸 막기 위해 정부에서는 햇살론, 사잇돌대출과 같은 ‘정책서민금융상품'이라는 걸 운영해요. 그 중 '햇살론뱅크'는 1금융권 대출이에요.",
"hardness":1,
"source":"Toss 금융 블로그",
"sourceUrl":"https://blog.toss.im/article/gov-subprime-loan",
"imgUrl":"https://static.toss-internal.com/ipd-tcs/toss_core/live/782287d4-7934-48d9-90c1-2f1f7ad2e8c6.png",
"imgAlt":"햇살론뱅크: 신용 낮은 사람이 1금융권 대출받는 법",
"publishedTime":"2023-03-27T15:00:00+09:00",
"click":None,
"like":None
}
]

Base.metadata.create_all(bind=engine)


def insert_test_data():
    db = SessionLocal()

    for article_data in test_articles:
        article = ArticleCreate(**article_data)
        create_article(db, article)
    db.close()


if __name__ == "__main__":
    insert_test_data()


