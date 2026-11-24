from pathlib import Path
import argparse,hashlib,json,re,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();problems=[];links=0;manifest_files=0
 for folder in ['research/001-cloud-ai-infrastructure','frameworks/proactive-threat-hunting']:
  package=ROOT/folder;manifest=json.loads((package/'evidence/source-manifest.json').read_text())
  for name,wanted in manifest.items():
   if hashlib.sha256((package/name).read_bytes()).hexdigest()!=wanted:problems.append('Tested source changed: '+folder+'/'+name)
   manifest_files+=1
 for path in ROOT.rglob('*.md'):
  for link in re.findall(r'\[[^\]]*\]\(([^)\s]+)\)',path.read_text()):
   if urllib.parse.urlparse(link).scheme or link.startswith('#'):continue
   raw=urllib.parse.unquote(link.split('#',1)[0].split('?',1)[0]);target=(path.parent/raw).resolve()
   if not target.is_relative_to(ROOT) or not target.exists():problems.append('Broken local link: '+path.relative_to(ROOT).as_posix()+' -> '+link)
   links+=1
 ledger=json.loads((ROOT/'migration/research-001-relocation.json').read_text())
 for entry in ledger['files']:
  if hashlib.sha256((ROOT/entry['new_path']).read_bytes()).hexdigest()!=entry['destination_sha256']:problems.append('Relocation destination changed: '+entry['new_path'])
 if ledger['original_files']!=40 or len(ledger['files'])!=40:problems.append('Original research coverage incomplete')
 research=json.loads((ROOT/'research/001-cloud-ai-infrastructure/evidence/summary.json').read_text());hunting=json.loads((ROOT/'frameworks/proactive-threat-hunting/evidence/summary.json').read_text())
 if research['unit_test_methods']!=13 or hunting['regression_test_methods']!=19:problems.append('Unexpected regression coverage')
 if research['synthetic_fixture_cases']!=144 or hunting['synthetic_scenarios']!=34:problems.append('Scenario coverage differs')
 for v in (research,hunting):
  if not all(v['isolation'][k] for k in ('external_network_unreachable','root_read_only','workspace_read_only')):problems.append('Isolation evidence missing')
 for path in ROOT.rglob('*'):
  if path.is_file() and '__pycache__' not in path.parts and not path.name.endswith('.pyc'):
   text=path.read_text()
   if re.search(r'AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}',text):problems.append('Potential credential in '+path.relative_to(ROOT).as_posix())
 result={'research_package':'research/001-cloud-ai-infrastructure','hunting_package':'frameworks/proactive-threat-hunting','original_files_relocated':40,'unchanged_original_bytes':ledger['bytes_unchanged_files'],'local_markdown_links_checked':links,'package_source_hashes_checked':manifest_files,'research':research,'hunting':hunting,'scope':'Structural preservation, source/link checks and isolated synthetic reference tests; no live provider/customer validation','problems':problems}
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'links':links,'source_hashes':manifest_files,'problems':problems},indent=2))
 if problems:raise SystemExit(1)
if __name__=='__main__':main()
