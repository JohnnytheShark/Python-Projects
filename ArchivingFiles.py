'''Function I used inside a class component to archive some csv files'''
def archiveAllFormerFiles(self):
        '''Function used to archive all the former files'''
        try:
            YesterdaysMonthlyFiles = glob.glob(f'{self.Folder}*Filename.CSV')
            YesterdaysDailyFiles = glob.glob(f'{self.Folder}*Filename.CSV')
            AllFiles = YesterdaysMonthlyFiles + YesterdaysDailyFiles
            with zipfile.ZipFile(f'{self.Folder}Archive/{AbbrDate}Outbound.zip', 'w') as archive:
                for file in AllFiles:
                    archive.write(self.Folder + os.path.basename(file), os.path.basename(file))
            logger.info("Able to archive all former Files")
            return True
        except:
            logger.error("Unable to Archive Files")
