import wx


class ListModel:

    def items(self):
        for i in range(100):
            yield (i, i * 2, i * 4)

    def columns(self):
        return ("one", "two", "three")


class AppFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetBackgroundColour((255, 255, 255))
        self.list = wx.ListCtrl(self, style=wx.LC_REPORT | wx.NO_BORDER)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.model = ListModel()
        self.UpdateItems()

    def SetModel(self, model):
        self.model = model

    def UpdateItems(self):
        self.list.ClearAll()
        for col in self.model.columns():
            self.list.AppendColumn(col)
        for item in self.model.items():
            self.list.Append(item)


def main():
    app = wx.App(redirect=False)
    AppFrame(None, title="Example App").Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
