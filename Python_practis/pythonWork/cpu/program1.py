import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        'https://www.google.com/search?q=image&sxsrf=APq-WBt3uSo7VsfINfVny_wbym8IAP93yg:1646728913150&tbm=isch&source=iu&ictx=1&vet=1&fir=nH5liarSz56duM%252C0JWe7yDOKrVFAM%252C_%253BDH7p1w2o_fIU8M%252CBa_eiczVaD9-zM%252C_%253Bn5hAWsQ-sgKo_M%252C-UStXW0dQEx4SM%252C_%253Bz4_uU0QB2pe-SM%252C7SySw5zvOgPYAM%252C_%253B2DNOEjVi-CBaYM%252CAOz9-XMe1ixZJM%252C_%253BMOAYgJU89sFKnM%252CygIoihldBPn-LM%252C_%253BxE4uU8uoFN00aM%252CpEU77tdqT8sGCM%252C_%253BqXynBYpZpHkhWM%252C4O2GvGuD-Cf09M%252C_%253B0DzWhtJoQ1KWgM%252CcIQ7wXCEtJiOWM%252C_%253BA4G7eW2zetaunM%252Cl3NoP295SYrYvM%252C_%253BbDjlNH-20Ukm8M%252CG9GbNX6HcZ2O_M%252C_%253BY6pVL1x5vDTXyM%252C6CoFeFXzCIyxLM%252C_&usg=AI4_-kTdhd_FHeViyMseasNFPsR3nR_Zcw&sa=X&ved=2ahUKEwjltKKfj7b2AhWGs1YBHQvoBckQ9QF6BAggEAE#imgrc=DH7p1w2o_fIU8M'
    ] * 1
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")