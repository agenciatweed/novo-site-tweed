import unittest
from bs4 import BeautifulSoup
from editorial_sources import render_sources
class SourcesTest(unittest.TestCase):
 def test_label_and_notes(self):
  s=BeautifulSoup(render_sources('NRF/Prosper, comunicado de 20/10/2026: https://example.org/report\n\nNota preservada.'),'html.parser');self.assertEqual(s.a.get_text(),'NRF/Prosper, comunicado de 20/10/2026');self.assertEqual(s.a['href'],'https://example.org/report');self.assertEqual(s.find_all('p')[1].get_text(),'Nota preservada.')
 def test_multiple_and_markdown(self):
  s=BeautifulSoup(render_sources('Fonte A: https://example.org/a\n[Fonte B](https://example.org/b)'),'html.parser');self.assertEqual([a.get_text() for a in s.find_all('a')],['Fonte A','Fonte B'])
 def test_plain_notes_and_empty(self):
  self.assertEqual(render_sources('  '),'');self.assertEqual(render_sources('Nota sem URL.'),'<p>Nota sem URL.</p>')
 def test_no_executable_markup(self):
  s=BeautifulSoup(render_sources('<script>alert(1)</script> [x](javascript:alert(1))'),'html.parser');self.assertIsNone(s.script);self.assertIsNone(s.a)
if __name__=='__main__':unittest.main()
