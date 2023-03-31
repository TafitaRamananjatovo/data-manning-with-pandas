import os
import time
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem, QMessageBox
import ui_main
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.load_file.clicked.connect(self.open_file)
        self.ui.traitment.clicked.connect(self.traitement)
        self.ui.show_items.clicked.connect(self.dataHead)
        self.ui.export_file.clicked.connect(self.exportation)

        self.path = None
        self.all_data = None
        self.final_data = None


    def open_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV (*.csv)")
        file_dialog.setDefaultSuffix("csv")
        file_dialog.setDirectory(os.getenv('ImportExportCsv'))
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.path = file_dialog.selectedFiles()[0]
            self.all_data = pd.read_csv(self.path, encoding='latin-1', low_memory=False)
            self.ui.file_name.setText(self.path)

    def traitement(self):
        needs_columns = ['Sku Code', 'Style Code', 'Style Name', 'Colour Name', 'Size Code', 'Specification',
                         'Retail Description',
                         'Product Feature 1', 'Product Feature 2', 'Product Feature 3',
                         'Washing Instructions', 'Fabric', 'Product Type', 'Single Price', 'Item Weight in KG',
                         'Colour Image']

        output_file = self.all_data[needs_columns]
        final_output = output_file.rename(
            columns={'Sku Code': 'SKU', 'Style Code': 'Parent', 'Style Name': 'Name',
                     'Colour Name': 'Attribute 1 value(s)',
                     'Size Code': 'Attribute 2 value(s)',
                     'Specification': 'Short Description',
                     'Retail Description': 'Description',
                     'Product Feature 1': 'Meta: product-feature-1',
                     'Product Feature 2': 'Meta: product-feature-2',
                     'Product Feature 3': 'Meta: product-feature-3',
                     'Washing Instructions': 'Meta: washing-instructions',
                     'Fabric': 'Meta: fabric', 'Product Type': 'Categories',
                     'Single Price': 'Regular price', 'Item Weight in KG': 'Weight (kg)',
                     'Colour Image': 'Images'})

        final_output.insert(0, "Type", "")
        final_output.insert(4, "Published", 1)
        final_output.insert(5, "Is featured?", 0)
        final_output.insert(6, "Allow customer reviews?", 1)
        final_output.insert(7, "Visibility in catalogue", "visible")
        final_output.insert(8, "Attribute 1 name", "")
        final_output.insert(10, "Attribute 1 default", "")
        final_output.insert(11, "Attribute 1 visible", "")
        final_output.insert(12, "Attribute 1 global", "")
        final_output.insert(13, "Attribute 2 name", "")
        final_output.insert(15, "Attribute 2 default", "")
        final_output.insert(16, "Attribute 2 visible", "")
        final_output.insert(17, "Attribute 2 global", "")

        # Singles values conditions
        single_conditions_1 = final_output['Parent'] == ""
        single_condition_2 = final_output['Attribute 1 value(s)'] == ""
        # Variable values conditions

        variable_condition_1 = final_output['Type'] == "variable"

        # Variation values conditions

        variation_condition_1 = final_output['Description'] == ""
        variation_condition_2 = final_output['Categories'] == ""

        # Les mises en valeurs
        final_output.loc[single_conditions_1 & single_condition_2, 'Type'] = "single"

        final_output.loc[single_conditions_1 == False, ['Type', 'Attribute 1 name', 'Attribute 2 name']] = [
            "variation", "color", "size"]

        data_reverse = final_output.iloc[::-1]
        count = 0

        mask = data_reverse['Parent'] != data_reverse['Parent'].shift(1)
        filtered_df = data_reverse[mask]

        new_rows = []
        for i, row in filtered_df.iterrows():
            new_row = {
                "Type": "variable",
                "SKU": row['Parent'],
                "Name": row['Name'],
                "Published": 1,
                "Is featured?": 0,
                "Allow customer reviews?": 1,
                "Visibility in catalogue": row['Visibility in catalogue'],
                "Attribute 1 default": "",
                "Attribute 1 name": row['Attribute 1 name'],
                "Attribute 1 visible": row['Attribute 1 visible'],
                "Attribute 1 global": "",
                "Parent": "",
                "Attribute 1 value(s)": "",
                "Attribute 2 default": "",
                "Attribute 2 name": row['Attribute 2 name'],
                "Attribute 2 value(s)": "",
                "Attribute 2 visible": "",
                "Attribute 2 global": "",
                "Short Description": row['Short Description'],
                "Description": row['Description'],
                "Meta: product-feature-1": row['Meta: product-feature-1'],
                "Meta: product-feature-2": row['Meta: product-feature-2'],
                "Meta: product-feature-3": row['Meta: product-feature-3'],
                "Meta: washing-instructions": row['Meta: washing-instructions'],
                "Meta: fabric": row['Meta: fabric'],
                "Categories": row['Categories'],
                "Regular price": "", "Weight (kg)": "",
                'Images': ""
            }
            new_rows.append(new_row)

        new_df = pd.DataFrame(new_rows)

        data_reverse = pd.concat([data_reverse, new_df], ignore_index=True)
        self.data_final = data_reverse.iloc[::-1]
        self.data_final = self.data_final.reset_index(drop=True)

        result_final_one = []
        result_final_two = []
        grouped_data = self.data_final.groupby('Parent')
        for group, data in grouped_data:
            col3_values_1 = data['Attribute 1 value(s)'].tolist()
            col3_values_2 = data['Attribute 2 value(s)'].tolist()
            result_final_one.append(col3_values_1)
            result_final_two.append(col3_values_2)

        my_list_one = [[x for x in inner_list if x != ''] for inner_list in result_final_one]
        my_list_one = [x for x in my_list_one if x != []]
        final_list_one = [list(set(subL)) for subL in my_list_one]

        my_list_two = [[x for x in inner_list if x != ''] for inner_list in result_final_two]
        my_list_two = [x for x in my_list_two if x != []]
        final_list_two = [list(set(subL)) for subL in my_list_two]

        for i, row in self.data_final.iterrows():
            if row['Parent'] == "":
                my_string_1 = ', '.join(map(str, final_list_one[i]))
                my_string_2 = ', '.join(map(str, final_list_two[i]))
                self.data_final.at[i, 'Attribute 1 value(s)'] = my_string_1
                self.data_final.at[i, 'Attribute 2 value(s)'] = my_string_2
        count = 0
        for i in range(100):
            count +=1
            time.sleep(0.0)
            self.ui.progressBar.setValue(count)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Treatment in success")
        msgBox.setWindowTitle("Message Box")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def dataHead(self):
        numColomn = self.ui.spin_items.value()
        if numColomn == 0:
            NumRows = len(self.data_final.index)
            print(NumRows)
        else:
            NumRows = numColomn
        self.ui.list_content_file.setColumnCount(len(self.data_final.columns))
        self.ui.list_content_file.setRowCount(NumRows)
        self.ui.list_content_file.setHorizontalHeaderLabels(self.data_final.columns)

        for i in range(NumRows):
            for j in range(len(self.data_final.columns)):
                self.ui.list_content_file.setItem(i, j, QTableWidgetItem(str(self.data_final.iat[i, j])))

        self.ui.list_content_file.resizeColumnsToContents()
        self.ui.list_content_file.resizeRowsToContents()
        count = 0
        for i in range(100):
            count += 1
            time.sleep(0.0)
            self.ui.progressBar.setValue(count)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Treatment in success")
        msgBox.setWindowTitle("Message Box")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def show_export_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path = QFileDialog.getExistingDirectory(self, "select directory", options=options)
        self.ui.path_for_exporting_file.setText(path)
        return path

    def exportation(self):
        if self.ui.csv.isChecked():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            path = QFileDialog.getExistingDirectory(self, "select directory", options=options)
            output = "output.csv"
            self.data_final.to_csv(f"{path}/{output}", index=False)
            self.output_view = pd.read_csv(f"{path}/{output}", encoding='ISO-8859-1', low_memory=False)
            path_ = os.path.abspath(f"{path}/{output}")
            self.ui.path_for_exporting_file.setText(path_)
            count = 0
            for i in range(100):
                count += 1
                time.sleep(0.0)
                self.ui.progressBar.setValue(count)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Treatment in success")
            msgBox.setWindowTitle("Message Box")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        elif self.ui.xls.isChecked():
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            path = QFileDialog.getExistingDirectory(self, "select directory", options=options)
            output = "output.xlsx"
            self.data_final.to_excel(f"{path}/{output}",engine='openpyxl', index=False)
            path_ = os.path.abspath(f"{path}/{output}")
            self.ui.path_for_exporting_file.setText(path_)
            count = 0
            for i in range(100):
                count += 1
                time.sleep(0.0)
                self.ui.progressBar.setValue(count)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Treatment in success")
            msgBox.setWindowTitle("Message Box")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def ShowProgressBar(self):
        if self.ui.load_file.isChecked():
            self.ui.export_file.clicked.connect(self.open_file)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Successfully")
            msgBox.setWindowTitle("Message Box")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        if self.ui.traitment.isChecked():
            self.ui.export_file.clicked.connect(self.traitement)

        if self.ui.show_items.isChecked():
            self.ui.export_file.clicked.connect(self.dataHead)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Successfully")
            msgBox.setWindowTitle("Message Box")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        if self.ui.export_file.isChecked():
            self.ui.export_file.clicked.connect(self.exportation)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Successfully")
            msgBox.setWindowTitle("Message Box")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
        """
        count = 0
        for i in range(100):
            
            count += 10
            time.sleep(0.0)
            self.ui.progressBar.setValue(count)
        """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())