import { OtkPage } from './app.po';

describe('otk App', function() {
  let page: OtkPage;

  beforeEach(() => {
    page = new OtkPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
